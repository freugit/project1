import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print("func_1 starting......")
    lock_1.acquire()
    print("func_1 申请了lock1")
    time.sleep(2)
    print("func_1 等待lock2")
    lock_2.acquire()
    print("func_1 申请了lock2")
    lock_2.release()
    print('func_1 释放了lock2')
    lock_1.release()
    print("func_1 释放了Lock1")
    print("func_1 Done")

def func_2():
    print("func_2 starting......")
    lock_2.acquire()
    print("func_2 申请了lock2")
    time.sleep(4)
    print("func_2 等待lock1")
    lock_1.acquire()
    print("func_2 申请了lock1")
    lock_1.release()
    print('func_2 释放了lock1')
    lock_2.release()
    print("func_2 释放了Lock2")
    print("func_2 Done")

if __name__ == "__main__":
    print("主程序启动")
    t1 = threading.Thread(target=func_1,args=())
    t2 = threading.Thread(target=func_2,args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("主程序结束")
