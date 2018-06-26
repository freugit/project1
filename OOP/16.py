import time
import threading
def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")
print("Main thread")
t1 = threading.Thread(target=fun,args=())
t1.setDaemon(True) #必须在启动前设置守护进程
t1.start()

time.sleep(1)
print("Main thread end")