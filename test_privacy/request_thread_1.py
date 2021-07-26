import time
import threading
from datetime import datetime
import requests
from functools import wraps
from bs4 import BeautifulSoup

#列表生成式生成urls列表
urls = [f"https://www.cnblogs.com/#p{i}" for i in range(1, 3+1)]


def log_print(fun):
    start_time = datetime.now()
    @wraps(fun)
    def log_out(*args, **kw):
        #start_time = time.ctime()
        print("程序开始时间是%s" % (start_time))

        fun(*args, **kw)
        #time.sleep(2)

        end_time = datetime.now()
        print("程序结束时间是%s" % (end_time))
        print("程序运行时间是%s" % (end_time-start_time))
    return log_out

def spider(urls):
    r = requests.get(urls)

    print(urls)
    print(len(r.text))

@log_print
def single_spider(urls):
    for i in urls:
        m = BeautifulSoup(requests.get(i).text, "html.parser").find_all("a",class_="post-item-title")
        for l in m:

            print(l["href"])
            print(l.get_text())
        print(m)
        return [(x["href"], x.get_text()) for x in m]

@log_print
def thread_spider(urls):
    thread = []
    for i in urls:
        thread.append(threading.Thread(target=spider,args=(i,)))
    for i in thread:
        i.start()
    for i in thread:
        i.join()

if __name__ == "__main__":
    single_spider(urls)
    #thread_spider(urls)







