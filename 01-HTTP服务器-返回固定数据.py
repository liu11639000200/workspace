import socket


def main():
    """创建服务器套接字，等待浏览器请求，返回一个数据给浏览器展示"""
    # 初始化服务器套接字
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 服务器地址要重用，必须要有这行代码
    server_soc.bind(("", 1315))
    server_soc.listen(128)

    # 获取客户端连接
    client_soc, client_addr = server_soc.accept()

    # 接收请求头数据
    print('准备接收数据')
    request_data = client_soc.recv(1024).decode('utf-8')
    print(request_data)

    # 返回一个网页给浏览器
    response_head = 'HTTP/1.1 200 OK\r\n'  # 为了适配 windows 系统，换行必须使用 \r\n
    response_head += '\r\n'
    response_body = 'hello'
    client_soc.send(response_head.encode('utf-8'))
    client_soc.send(response_body.encode('utf-8'))

    # 关闭客户端套接字
    client_soc.close()

    # 关闭服务器套接字
    server_soc.close()


if __name__ == '__main__':
    main()
