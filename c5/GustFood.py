# To caculate how mang food guest brought
"""
The output of this program looks like this:

Number of things being brought: 
- Apples 7
- Cups 3
- Cakes 0
- Ham Sandwiches 3 
- Apple Pies 1
"""

allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 
'Bob': {'ham sandwiches': 3, 'apples': 2}, 
'Carol': {'cups': 3, 'apple pies': 1}}

allThings = {}
total = 0
for k, v in allGuests.items():
    for vk, vv in v.items():
        total += vv
        if vk in allThings.keys():
            allThings[vk] = allThings[vk] + vv
        else:
            allThings[vk] = vv

print(allThings)
print("Number of things being brought:")

for k, v in allThings.items():
    print(f" - {k}   {v}")

