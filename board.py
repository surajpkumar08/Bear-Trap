import random

import common

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board

    def get_board_value(self, x: int, y: int):
        return self.board[x][y]

    def check_boundary(self, x: int, y: int):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return True
        return False

    # Display the board game
    def display_board(self, bear_coordinate: tuple):
        color_map, direction = common.get_colour_map(), common.get_direction()

        move_set = []
        for d in direction[bear_coordinate[0] % 2]:
            x, y = bear_coordinate[0] + d[0], bear_coordinate[1] + d[1]
            if x < 0 or x >= self.size or y < 0 or y >= self.size or self.get_board_value(x,y) != ".":
                continue
            move_set.append((x, y))

        for row in range(self.size):
            if row % 2 == 1:
                print("    ", end="")
            for col in range(self.size):
                if self.board[row][col] in ["B", "BL", "#", "F"]:
                    color_emoji = color_map[self.board[row][col]]
                    print(f"{color_emoji[0]}{color_emoji[1]} {color_map['R']}", end=" ", flush=True)
                    continue

                coordinate = f"{row},{col}".center(5)
                if (row, col) in move_set:
                    print(f"{color_map['M']}({coordinate}) {color_map['R']}", end=" ", flush=True)
                else:
                    print(f"{color_map['.']}({coordinate}) {color_map['R']}", end=" ", flush=True)
            print("\n", flush=True)

    # Populate with Missile and Fish
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

    def populate_missile(self, missile_count: int):
        self.populate_board(missile_count, "#")


    def populate_bear(self, old_bear_coordinate: tuple, bear: 'Bear'):
        if bear.bear_captured_state():
            self.board[old_bear_coordinate[0]][old_bear_coordinate[1]] = "BL"
            return

        self.board[old_bear_coordinate[0]][old_bear_coordinate[1]] = "."
        if not bear.bear_free_state():
            self.board[bear.get_x()][bear.get_y()] = "B"

    def populate_missile_by_user(self, missile_coordinate: tuple, agent: 'CatAgent'):
        if self.get_board_value(missile_coordinate[0],missile_coordinate[1]) == "F":
            agent.set_fish_point(common.get_fish_score("HIT"))
        self.board[missile_coordinate[0]][missile_coordinate[1]] = "#"

        #Easter egg
        if agent.agent_name == "raeb":
            self.board[missile_coordinate[0]][missile_coordinate[1]] = "."
