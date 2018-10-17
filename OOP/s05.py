"""
Client端流程：
        1.建立通信socket
        2.链接对方，请求跟对方建立通路
        3.发送内容到对方服务器
        4.接受对方的反馈
        5.关闭链接通路
"""

import socket

def tcp_clt():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = ("127.0.0.1",8998)
    sock.connect(addr)
    msg = "I love wangxiaojing"
    sock.send(msg.encode())
    rst = sock.recv(500)
    print(rst.decode())
    sock.close()

if __name__ == "__main__":
    tcp_clt()



