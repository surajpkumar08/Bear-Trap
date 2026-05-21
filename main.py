from rich.prompt import InvalidResponse

from bear import Bear
from board import Board

if __name__ == '__main__':
    board = Board(11)
    bear = Bear(5, 5)

    board.populate_bear(bear.get_bear_coordinates(), bear.get_bear_coordinates())
    board.populate_wall(15)
    board.populate_fish(5)

    board.display_board(bear.get_bear_coordinates())

    value = "Play"
    while value != "Lost" and value != "Won":
        try:
            user_choice = input("Enter your choice x y : ")
            wall_x, wall_y = user_choice.split(" ")
            if board.check_boundary(int(wall_x), int(wall_y)):
                raise InvalidResponse("You can't build the wall outside the zone!")
            board.populate_wall_by_user((int(wall_x), int(wall_y)))
        except ValueError or IndexError:
            print("Invalid Input, try again! It must be integer - x y")
            continue
        except InvalidResponse as e:
            print(e)
            continue

        bear_coordinate = bear.get_bear_coordinates()
        bear.move_bear(board)
        if bear.get_bear_coordinates() == (-1, -1):
            board.display_board(bear.get_bear_coordinates())
            value = "Lost"
            break

        board.populate_bear(bear_coordinate, bear.get_bear_coordinates())
        board.display_board(bear.get_bear_coordinates())
        if bear.get_x() == 0 or bear.get_y() == 0 or bear.get_x() == board.get_size()-1 or bear.get_y() == board.get_size()-1:
            value = "Won"

    print(f"The bear {value}")