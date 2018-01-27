import socket
import re


def handle_client(client_soc):
    """处理一个客户端的请求"""
    print('准备接收数据')
    request_data = client_soc.recv(1024).decode('utf-8')
    # print('请求头：\n', request_data)
    if request_data:
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
            response_head += '\r\n'
            response_body = content
            client_soc.send(response_head.encode('utf-8'))
            client_soc.send(response_body)

    # 关闭客户端套接字
    client_soc.close()


def main():
    """创建服务器套接字，等待浏览器请求，返回一个数据给浏览器展示"""
    # 初始化服务器套接字
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 服务器地址要重用，必须要有这行代码
    server_soc.bind(("", 1315))
    server_soc.listen(128)

    while True:
        # 获取客户端连接
        client_soc, client_addr = server_soc.accept()

        # 接收请求头数据
        handle_client(client_soc)

    # 关闭服务器套接字
    server_soc.close()


if __name__ == '__main__':
    main()
