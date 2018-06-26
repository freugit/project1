"""
利用time函数，生成两个函数
顺序调用
计算总的运行时间
"""
import time
import _thread as thread
def loop1():
    # ctime得到当前时间
    print("Start loop 1 at:",time.ctime())
    # 睡眠一段时间，单位是秒
    time.sleep(4)
    print("End loop 1 at:",time.ctime())
def loop2():
    # ctime得到当前时间
    print("Start loop 2 at:",time.ctime())
    # 睡眠一段时间，单位是秒
    time.sleep(2)
    print("End loop 2 at:",time.ctime())

def main():
    print("Starting at:",time.ctime())
    #loop1()
    #loop2()
    #上面原来的代码改成如下：
    thread.start_new_thread(loop1,())
    # 启动多线程的意思是用多线程去执行某个函数，启动多线程的函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，第二是函数的参数作为元组使用，为空，则使用空元组
    # 注意，如果函数只有一个参数，需要参数后要有一个逗号
    thread.start_new_thread(loop2,())

    print("All done at",time.ctime())


if __name__ == "__main__":
    main()
    while True:
        time.sleep(1)   #为了避免主线程提早结束，用无限循环等。。。
