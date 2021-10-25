# import time, datetime
# def calcProd():
# # Calculate the product of the first 100,000 numbers. 
# 	product = 1
# 	for i in range(1, 100000):
# 		product = product * i 
# 	return product

# startTime = time.time() 
# prod = calcProd()
# endTime = time.time()

# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))

# print(type(time.time()))

# for i in range(10,3,-1):
#     print(i)

# dt = datetime.datetime.now()
# day_1000 = datetime.timedelta(days=1000)
# print(dt + day_1000)

# import threading, time
# print('Cats', 'Dogs', 'Frogs', sep=' & ')
# print("Start of program.")

# def takeANap(): 
# 	time.sleep(5)
# 	print("Wake up!")

# threadObj = threading.Thread(target=takeANap)
# threadObj.start() 
# print('End of program.')

import subprocess
subprocess.Popen(['open', '/System/Applications/Calculator.app'])