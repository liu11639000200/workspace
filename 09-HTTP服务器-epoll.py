import socket
import re
import select


def handle_client(client_soc, request_data):
    """处理一个客户端的请求"""
    print('准备接收数据')
    # 浏览器有数据发送来，才读取文件内容
    first_line = request_data.splitlines()[0]
    print(first_line)
    file_path = re.match(r'[^/]+(/[^ ]*)', first_line).group(1)

    if file_path == '/':  # 访问根目录是返回首页数据
        file_path = '/index.html'
    print(file_path)


    try:
        # 获取到文件内容
        with open('html'+file_path, 'rb') as f:
            content = f.read()

    except:
        # 文件不存在
        response_head = 'HTTP/1.1 404 NOT FOUND\r\n'
        response_head += 'Content-Type: text/html;charset=utf-8\r\n'  # 告诉浏览器，服务器发送的字符是 utf-8 编码的
        response_head += '\r\n'
        response_body = '无法打开文件'
        client_soc.send(response_head.encode('utf-8'))
        client_soc.send(response_body.encode('utf-8'))

    else:
        # 返回一个网页给浏览器
        response_head = 'HTTP/1.1 200 OK\r\n'  # 为了适配 windows 系统，换行必须使用 \r\n
        response_head += 'Content-Length:%d\r\n' % len(content)  # 获取文件长度
        response_head += '\r\n'
        response_body = content
        client_soc.send(response_head.encode('utf-8'))
        client_soc.send(response_body)

    # 关闭客户端套接字
    # client_soc.close()


def main():
    """创建服务器套接字，等待浏览器请求，返回一个数据给浏览器展示"""
    # 初始化服务器套接字
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 服务器地址要重用，必须要有这行代码
    server_soc.bind(("", 1315))
    server_soc.listen(128)

    # 创建 epoll 对象
    epoll = select.epoll()

    # 注册服务器套接字到 epoll
    epoll.register(server_soc.fileno(), select.EPOLLIN)


    client_dict = {}
    while True:
        # 等待客户端事件发生，这个方法是阻塞式的
        fd_list = epoll.poll()

        # 遍历每一个发生事件的套接字并处理
        for fd, event in fd_list:

            if fd == server_soc.fileno():
                # 服务器有事件发生，一般就是有新客户端连接
                client_soc,client_addr = server_soc.accept()

                # 注册新的客户端套接字到 epoll
                epoll.register(client_soc.fileno(), select.EPOLLIN)

                # 把新客户端保存到字典里,使用当前客户端的文件描述符作为关键字
                client_dict[client_soc.fileno()] = client_soc

            else:
                # 有客户端事件发生
                client_soc = client_dict[fd]
                recv_data = client_soc.recv(1024).decode('utf-8')

                if recv_data:
                    handle_client(client_soc, recv_data)
                else:
                    # 数据为空，客户端已经关闭连接.资源回收
                    client_soc.close()
                    del client_dict[fd]
                    epoll.unregister(fd)


    # 关闭服务器套接字
    server_soc.close()


if __name__ == '__main__':
    main()
