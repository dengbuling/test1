import time
import threading
from datetime import datetime
import requests
from functools import wraps
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/#p{i}" for i in range(1, 50+1)]
def single_spider(urls):
    for i in urls:
        r = requests.get(i)
        x = r.text
        m = BeautifulSoup(x, "lxml").find(class_="post-item-title")
        print(m)
single_spider(urls)