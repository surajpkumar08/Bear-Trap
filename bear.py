import random
import common
from board import Board


class Bear:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.bear_captured = False
        self.bear_free = False

    def find_shortest_path(self, board: 'Board'):
        size, direction = board.get_size(), common.get_direction()

        queue = []
        visited = {self.get_bear_coordinates()}
        for d in direction[self.get_x() % 2]:
            x, y = self.get_x() + d[0], self.get_y() + d[1]
            if board.check_boundary(x,y) or board.get_board_value(x,y) == "#":
                continue
            queue.append((x, y, (x, y)))
            visited.add((x, y))

        if len(queue) == 0:
            # Detention cell coordinates
            return -8, -8

        random_move = random.choice(queue)[2]

        while queue:
            x, y, parent = queue.pop(0)
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                return parent

            for d in direction[x % 2]:
                candi_x, candi_y = x + d[0], y + d[1]
                if (board.check_boundary(candi_x, candi_y)
                        or board.get_board_value(candi_x, candi_y) == "#" or (candi_x, candi_y) in visited):
                    continue
                queue.append((candi_x, candi_y, parent))
                visited.add((candi_x, candi_y))

        return random_move

    def move_bear(self, board: 'Board'):
        self.x, self.y = self.find_shortest_path(board)
        if self.x == -8 and self.y == -8:
            self.bear_captured = True
        if self.x == 0 or self.y == 0 or self.x == board.get_size() - 1 or self.y == board.get_size() - 1:
            self.bear_free = True
            # Escape coordinates
            self.x, self.y = -100, -100

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_bear_coordinates(self):
        return self.x, self.y

    def bear_captured_state(self):
        return self.bear_captured

    def bear_free_state(self):
        return self.bear_free

    def get_bear_image(self):
        if self.bear_free:
            return common.bear_free()
        if self.bear_captured:
            return common.jailed_bear()
        return common.wanted_bear(self.get_bear_coordinates())