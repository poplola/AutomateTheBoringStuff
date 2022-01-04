# import requests
# from bs4 import BeautifulSoup

# url = "https://www.cnn.com"

# response = requests.get(url)
# response.raise_for_status()

# print(type(response.content))

# with open("d.html", 'bw') as f:
#     f.write(response.content)

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        total = time.time() - start
        print()
        print(func)
        print(' '.join(str(func)[1:].split(' ')[:2]))
        print(f"total run seconds : {total}")
    return wrapper


@timer
def test1():
    for _ in range(1000000):
        pass


@timer
def test2():
    for _ in range(10000000):
        pass


test1()
test2()