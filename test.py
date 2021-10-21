# find index number of capital letter
s = "HeLLo wOrLD!"
new = [index for index, value in enumerate(s) if value.isupper()]
print(new)
