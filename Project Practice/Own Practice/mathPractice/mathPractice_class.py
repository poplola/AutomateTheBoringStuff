"""
    - Class edition
    - Help Adam to practice math +-×÷ within 12 and 100
"""

import random, os

class Math:
    add_sub_min = 5
    add_sub_max = 100
    mul_div_min = 2
    mul_div_max = 12
    rows = 400
    cols = 4

    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0

    def num_choice(self, n_min, n_max):
        self.n1 = random.randint(n_min, n_max)
        self.n2 = random.randint(n_min, n_max)

    def add_sub(self):
        self.num_choice(self.add_sub_min, self.add_sub_max)
        self.n3 = self.n1 + self.n2

    def mul_div(self):
        self.num_choice(self.mul_div_min, self.mul_div_max)
        self.n3 = self.n1 * self.n2

    def mixed(self, sign=['+','-','×','÷']):

        # Change file current working folder path 
        print(os.chdir("./Project Practice/Own Practice/mathPractice/"))

        with open("math_class.txt", 'w') as f:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.operator = random.choice(sign)
                    if self.operator in ['+','-']:
                        self.add_sub()
                    else:
                        self.mul_div()

                    if self.operator == '-' or self.operator == '÷':
                        self.n1 = self.n3
                    f.write(self.__repr__())
                    # print(self.__repr__(), end='')
                f.write('\n\n')
                # print('\n')

    def __repr__(self):
        s = f"{self.n1} {self.operator} {self.n2} =".ljust(20)
        return s

def main():
    operator_list = ['+','-','×','÷']
    math_excise = Math()
    # math_excise.mixed(operator_list[:2])    # ['+','-']
    # math_excise.mixed(operator_list[2:])      # ['×','÷']
    math_excise.mixed()     # ['+','-','×','÷']

if __name__ == "__main__":
    main()
