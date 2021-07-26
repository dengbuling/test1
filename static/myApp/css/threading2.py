import threading
import time
from datetime import datetime

def people(ThreadName):
    for i in range(1,10):
        time.sleep(1)
        print("在%s吃了%s只%s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i, ThreadName))
#people("龙虾")
def pink(ThreadName):
    for i in range(1,10):
        time.sleep(1)
        print("在%s吃了%s只%s"%(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i, ThreadName))
#pink("鲈鱼")
ted = []
ted1 = threading.Thread(target=people, args=("龙虾",))
ted.append(ted1)
ted2 = threading.Thread(target=pink, kwargs={"ThreadName":"鲈鱼"})


ted.append(ted2)

for i in ted:
    i.start()