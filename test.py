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
a.reverse()
print(a)