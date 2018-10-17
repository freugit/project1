import multiprocessing
from time import sleep,ctime


class ClockProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.__init__构造函数
    2.run函数
    '''
    def __init__(self,interval):
        super().__init__()
        self.interval = interval


    def run(self):
        while True:
            print("The time is " + ctime())
            sleep(self.interval)

if __name__ == "__main__":
    c = ClockProcess(5)
    c.start()


