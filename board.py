import os
import random

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.direction = [[[-1,-1],[-1,0],[0,-1],[0,1],[1,-1],[1,0]], [[-1,0],[-1,1],[0,-1],[0,1],[1,0],[1,1]]]

    #Display the board game
    def display_board(self, bear_coordinate: tuple):
        os.system('clear')

        color_map = {"B":["\033[93m","(ʕ•ᴥ•ʔ)"],
                     ".":"\033[34m",
                     "M":"\033[32m",
                     "F":["\033[31m","<•))>><"],
                     "#":["\033[37m","[#####]"],
                     "R":"\033[0m"}

        move_set = []
        for d in self.direction[bear_coordinate[0] % 2]:
            x, y = bear_coordinate[0] + d[0], bear_coordinate[1] + d[1]
            if x < 0 or x >= self.size or y < 0 or y >= self.size or self.board[x][y] != ".":
                continue
            move_set.append((x, y))

        for row in range(self.size):
            if row % 2 == 1:
                print("    ", end="")
            for col in range(self.size):
                if self.board[row][col] in ["B", "#", "F"]:
                    color_emoji = color_map[self.board[row][col]]
                    print(f"{color_emoji[0]}{color_emoji[1]} {color_map['R']}", end=" ", flush=True)
                    continue

                coordinate = f"{row},{col}".center(5)
                if (row, col) in move_set:
                    print(f"{color_map['M']}({coordinate}) {color_map['R']}", end=" ", flush=True)
                else:
                    print(f"{color_map['.']}({coordinate}) {color_map['R']}", end=" ", flush=True)
            print("\n", flush=True)

    #Populate with Wall and Fish
    def populate_board(self, count: int, board_char: str):
        while count > 0:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.board[row][col] != ".":
                continue
            self.board[row][col] = board_char
            count -= 1

    def populate_fish(self, fish_max_count: int):
        fish_count = random.randint(0, fish_max_count)
        self.populate_board(fish_count, "F")

    def populate_wall(self, wall_count: int):
        self.populate_board(wall_count, "#")

    def populate_bear(self, old_bear_coordinate: tuple, new_bear_coordinate: tuple):
        self.board[old_bear_coordinate[0]][old_bear_coordinate[1]] = "."
        self.board[new_bear_coordinate[0]][new_bear_coordinate[1]] = "B"

    def populate_wall_by_user(self, wall_coordinate: tuple):
        self.board[wall_coordinate[0]][wall_coordinate[1]] = "#"

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board

    def get_dir(self):
        return self.direction

    def check_boundary(self, x: int, y: int):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return True
        return False
