from board import Board
import random

class Bear:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def find_shortest_path(self, board: 'Board'):
        size, grid, direction = board.get_size(), board.get_board(), board.get_dir()

        queue = []
        visited = {self.get_bear_coordinates()}
        for d in direction[self.get_x() % 2]:
            x, y = self.get_x() + d[0], self.get_y() + d[1]
            if board.check_boundary(x,y) or grid[x][y] == "#":
                continue
            queue.append((x, y, (x, y)))
            visited.add((x, y))

        if len(queue) == 0:
            return -1, -1

        random_move = random.choice(queue)[2]

        while queue:
            x, y, parent = queue.pop(0)
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                return parent

            for d in direction[x % 2]:
                candi_x, candi_y = x + d[0], y + d[1]
                if (board.check_boundary(candi_x, candi_y)
                        or grid[candi_x][candi_y] == "#" or (candi_x, candi_y) in visited):
                    continue
                queue.append((candi_x, candi_y, parent))
                visited.add((candi_x, candi_y))

        return random_move

    def move_bear(self, board: 'Board'):
        self.x, self.y = self.find_shortest_path(board)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_bear_coordinates(self):
        return self.x, self.y


