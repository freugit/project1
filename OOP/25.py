import threading
import time

class myThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num += 1
            msg = self.name + "set num to " + str(num)
            print(msg)
            mutex.acquire()   #再次申请自己拥有的锁,如果不是可重入锁，会死等
            mutex.release()
            mutex.release()



num = 0
mutex = threading.RLock()  #可重入锁是RLock()

def test1():
    for i in range(5):
        t = myThread()
        t.start()

if __name__ == "__main__":
    test1()