import socket
"""
Server端的编写流程：
        1.建立socket负责具体通信，这个socket其实只负责接受对方的请求
        2.绑定端口和地址
        3.监听接入的访问socket
        4.接受访问的socket，可以理解接受访问建立了一个通信的链路通路
        5.接受对方的发送内容，利用接收到的socket接收内容
        6.如果有必要，给对方发送反馈信息
        7.关闭链接通路
"""
def tcp_srv():

    #建立socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    addr = ("127.0.0.1",8998)

    # 绑定地址
    sock.bind(addr)

    # 监听接入访问的socket
    sock.listen()

    while True:
        # 接受访问的socket，可以理解接受访问建立了一个通讯的链接通路
        # accept第一个元素赋值给skt，第二个赋值为addr
        skt,addr = sock.accept()

        # 接受对方的发送内容，利用接收到的socket接受内容
        msg = skt.recv(500)


        msg = msg.decode()

        rst = "Received msg:{0} from {1}".format(msg,addr)

        print(rst)
        # 如果有必要，给对方发送反馈信息
        skt.send(rst.encode())
        # 关闭链接通路
        skt.close()

if __name__ == "__main__":
    print("Starting Server...")
    tcp_srv()
