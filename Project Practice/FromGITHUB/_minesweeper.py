import random
from typing import Counter

class board():

    def __init__(self, board_size=5, bomb_num=2):
        self.board_size = board_size
        self.bomb_num = bomb_num
        self.dig_pos = -1
        self.board = [0 for r in range(self.board_size) for c in range(self.board_size)]
        self.board_show = ['' for r in range(self.board_size) for c in range(self.board_size)]
        self.bombs_pos = random.sample([i for i in range(self.board_size ** 2)], self.bomb_num)

        for pos in range(self.bomb_num):
            self.board[self.bombs_pos[pos]] = 'BOMB'
      

        for bomb_pos in self.bombs_pos:
            row = int(bomb_pos/self.board_size)
            col = bomb_pos % self.board_size
            print(bomb_pos, row, col)

            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if r not in range(self.board_size) or c not in range(self.board_size):
                        continue

                    num = r*self.board_size + c
                    if self.board[num] != 'BOMB':
                        self.board[num] = self.board[num] + 1

    def showBoard(self):
        for i in range(self.board_size):
            print(f"\t{i}", end="")
        print()

        if self.dig_pos != -1:
            self.showDigArea(self.dig_pos)

        print("=" * 100)        

        for i in range(len(self.board)):

            if ((i % (self.board_size)) == 0):
                print("\n")
                print(int(i/self.board_size), end="")

            print(f'\t{self.board[i]}', end="")      

        print()
        print("-" * 70)
        
        for i in range(len(self.board)):

            if ((i % (self.board_size)) == 0):
                print("\n")
                print(int(i/self.board_size), end="")
     
            print(f'\t{self.board_show[i]}', end="")  
        print()  
        
    def showDigArea(self, check_pos):
        self.board_show[check_pos] = self.board[check_pos]

        row = int(check_pos/self.board_size)
        col = int(check_pos%self.board_size)


        if self.board[check_pos] == 0:
            for r in range(row-1, row+2):
                if r < 0 or r >= self.board_size:
                    continue
                for c in range(col-1, col+2):
                    if c < 0 or c >= self.board_size:
                        continue   
                    num = r*self.board_size + c 
                    self.board_show[num] = self.board[num]


    def digBomb(self):
        dig_r, dig_c = input("\nWhere do you dig? Pls input row,col: ").split(",")
        print(dig_r, dig_c)

        self.dig_pos = int(dig_r) * self.board_size + int(dig_c)
        print(f"{self.dig_pos} = {dig_r} * {self.board_size} + {dig_c}")
        print(self.dig_pos)

        print(str(self.board[self.dig_pos]))

        if str(self.board[self.dig_pos]) == 'BOMB':
            print("\nGAME OVER!!!")
            self.board_show = self.board
            self.showBoard()            
            return False

        self.showBoard()

        if self.board_show.count('') == self.bomb_num:
            print(f"\nCongratuation! You found all {self.bomb_num} bombs.")
            self.board_show = self.board
            return False

        return True

play = board()
while True:
    if not play.digBomb():
        replay = input("\nDo you want to play again?(y/n) ")
        if replay.lower() == "n":
            break
        play.__init__()

print('\n'*2)