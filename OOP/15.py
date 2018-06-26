"""
利用time函数，生成两个函数
顺序调用
计算总的运行时间
"""
import time
import threading
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
    t2 = threading.Thread(target=loop2, args=())
    t1 = threading.Thread(target=loop1,args=())
    t1.start()
    t2.start()
    # threading启动多线程的方法是先实例化一个Thread，再用start()启动
    # 注意，如果函数只有一个参数，需要参数后要有一个逗号
    t1.join()
    t2.join()
    print("All done at",time.ctime())


if __name__ == "__main__":
    main()