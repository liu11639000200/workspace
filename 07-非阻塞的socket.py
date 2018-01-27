import socket
import time

def main():
    # 初始化 TCP 服务器
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 服务器地址要重用，必须要有这行代码
    server_soc.bind(("", 1315))
    server_soc.listen(128)

    # 设置套接字为非阻塞
    server_soc.setblocking(False)

    client_list = []
    while True:
        # 等待客户端连接
        time.sleep(1)

        try:
            client_soc, client_addr = server_soc.accept()
            # print('获取到新的客户端连接')
        except:
            print('发生异常，没有新的客户端连接进来-----')
        else:
            print('没有发生异常，有新的客户端连接进来---------------')
            client_soc.setblocking(False)
            client_list.append(client_soc)  # 保存套接字到列表里，供下一次循环使用

        # 在 try 语句的外面，使用 for 遍历列表里的所有客户端，尝试获取数据
        for client_soc in client_list[:]:
            try:
                recv_data = client_soc.recv(1024)
            except:
                print('发生异常，客户端没有发生新的数据过来++++++')
            else:
                if recv_data:
                    print('没有异常，客户端发送了新的数据过来+++++++++++++++++++', recv_data)
                else:
                    print('获取到的数据为空，说明客户端已经关闭了连接++++')
                    client_list.remove(client_soc)
                    client_soc.close()



    # 关闭服务器套接字
    server_soc.close()


if __name__ == '__main__':
    main()

