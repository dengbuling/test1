# coding=utf-8
import threading
import time
from queue import Queue
q = Queue(maxsize = 0)
#生产消费模型
def product(name):
    count = 1
    while True:
        q.put('产生出的第{}票'.format(count))
        print('{0}生产出第{1}票'.format(name,count))
        count+=1
        time.sleep(1)
        if count > 5:
            break
def consume(name):
    while True:
        print('{0}卖出了总部{1}'.format(name,q.get()))
        time.sleep(1)
        q.task_done()


class ticket_thread(threading.Thread):
    #lock = threading.Lock()
    def __init__(self,port,name):
        super(ticket_thread, self).__init__()
        self.port = port
        self.name = name
    def run(self):
        #self.lock.acquire()
        product(self.name)
        consume(self.name)
        # for i in range(1, 6):
        #     print("窗口%s正在%s%s张,当前线程%s" % (self.port, self.name,i,threading.current_thread()))
        #     time.sleep(0.5)
        #self.lock.release()


def main():

    t1 = ticket_thread("线程1","出票")
    t2 = ticket_thread("线程2", "售票")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

main()