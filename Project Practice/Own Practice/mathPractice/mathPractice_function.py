"""
    - Function edition
    - Help Adam to practice math +-×÷ within 12 and 500
"""

import random, os

# +- operation within 500
def add_sub(sign_a_s):
    # sign_a_s = random.choice(['+','-'])
    num_1 = random.randint(5, 100)
    num_2 = random.randint(5, 100)
    num_3 = num_1 + num_2
    return num_1, num_2, num_3, sign_a_s

# ×÷ function within 12
def multi_division(sign_m_d):
    # sign_m_d = random.choice(['×','÷'])
    num_1 = random.randint(2, 12)
    num_2 = random.randint(2, 12)
    num_3 = num_1 * num_2
    return num_1, num_2, num_3, sign_m_d

# +-×÷ mixed 
def mixed():
    sign = random.choice(signList)
    if sign == '+' or sign == '-':
        return add_sub(sign)
    else:
        return multi_division(sign)


rows = 400
col = 4
lenth = 20
n1, n2, n3 = 0, 0, 0
operator = ''
signList = ['+','-','×','÷']

# Change file current working folder path 
print(os.chdir("./Project Practice/Own Practice/mathPractice/"))

with open("math.txt", "w") as f:
    # f.write("========= x/÷ within 12 =========" + '\n')
    # f.write('\n')
    for row in range(rows):
        for i in range(col):
            # call fuction: '+','-'
            n1, n2, n3, operator = add_sub(random.choice(signList[:2]))

            # call function: '×','÷'     
            # n1, n2, n3, operator = multi_division(random.choice(signList[2:]))    

            # call function: '+','-','×','÷'
            # n1, n2, n3, operator = mixed()   

            if operator == '+' or operator == '×':
                f.write(f"{n1} {operator} {n2} =".ljust(lenth))
            else:
                f.write(f"{n3} {operator} {n2} =".ljust(lenth))
          
        f.write('\n'*2)    

   