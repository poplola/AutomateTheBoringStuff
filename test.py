# # find index number of capital letter
# s = "HeLLo wOrLD!"
# new = [index for index, value in enumerate(s) if value.isupper()]
# print(new)

# a = [1,2,3,4,3,2,1]
# b = list(set(a))

# # b = [ x for x in a if x in filter()]

# def dupl(x):
#     # c = str(x)
#     if x in b:
#         return x

# print(a, b)
# print(list(filter(dupl, a)))


# a = ['1', '2', '3', '4', '5']
a = [1,2,3,4,5]

# for item, index in enumerate(a):
#     print(item, index)

# len_a = len(a)-1
# print(a)
# for i in range(len_a, -1, -1):
#     print(i, a[i])
# a.reverse()
# print(a)


# import requests
# from bs4 import BeautifulSoup
 
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, "html.parser")
 
# for story_heading in soup.find_all(class_="story-heading"): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())

import random

num = random.randrange(10)
print(num)