from bear import Bear
from board import Board
from catAgent import CatAgent
from dataHandler import DataHandler

import common

def display_status(board, bear):
    common.clear_screen()
    print(bear.get_bear_image())
    board.display_board(bear.get_bear_coordinates())

def user_choice(user_input, board, agent : 'CatAgent'):
    try:
        x, y = user_input.split(" ")
        missile_x, missile_y = int(x), int(y)

        if board.check_boundary(missile_x, missile_y):
            # Easter Egg
            if missile_x>8111997 or missile_y>10022000:
                raise RuntimeError(f"\n\033[96m{common.funny_exception()}\033[0m\n")
            raise RuntimeError("\n\033[91mYOU CAN'T DROP THE MISSILE OUTSIDE THE ZONE! We can't obliterate the civilian sector\033[0m\n")
        if board.get_board_value(missile_x, missile_y) == "B":
            raise RuntimeError("\n\033[93mHOLD YOUR FIRE, AGENT! We need that target alive for questioning. Contain! not kill!\033[0m\n")

        board.populate_missile_by_user((missile_x, missile_y), agent)
        return True

    except (ValueError, IndexError):
        print("\n\033[93mPlease focus agent, no time to take nap!\033[0m\n")
    except RuntimeError as e:
        print(e)
    return False

def play_game(agent : 'CatAgent'):
    board = Board(11)
    bear = Bear(5, 5)

    board.populate_bear(bear.get_bear_coordinates(), bear)
    board.populate_missile(15)
    board.populate_fish(5)

    display_status(board, bear)
    value = "PLAY"
    while value != "LOST" and value != "WON":
        user_input = input(common.coordinate_input())
        if user_input.upper() == "ABORT":
            value = "ABORT"
            agent.set_fish_point(common.get_fish_score("ABORT"))
            agent.save_agent_data(dataHandler.data)
            break

        if not user_choice(user_input, board, agent):
            continue

        bear_coordinate = bear.get_bear_coordinates()
        bear.move_bear(board)
        board.populate_bear(bear_coordinate, bear)
        display_status(board, bear)

        if bear.bear_captured_state():
            value = "WON"
            agent.set_fish_point(common.get_fish_score("WON"))
            agent.set_wins()
            agent.save_agent_data(dataHandler.data)


        if bear.bear_free_state():
            value = "LOST"
            agent.set_fish_point(common.get_fish_score("LOST"))
            agent.save_agent_data(dataHandler.data)

    print(common.won_lost_banner(value, agent.agent_name))


def game_menu():
    while True:
        game_menu_input = input(common.game_menu())
        if game_menu_input in ["1","2","3","4","5","6"]:
            return game_menu_input
        else:
            print("All okay agent? Had a little extra yesterday?")

def start_game(dataHandler, user_name):
    cat_agent = CatAgent(user_name)
    new_player = cat_agent.load_agent(dataHandler.data)
    if new_player:
        print(common.game_instructions(cat_agent))

    while True:
        choice = game_menu()
        common.clear_screen()
        if choice == "1":
            play_game(cat_agent)
        elif choice == "2":
            common.exit_game_print()
            break
        elif choice == "3":
            print(common.game_instructions(cat_agent))
        elif choice == "4":
            print(cat_agent.agent_stats())
        elif choice == "5":
            cat_agent.show_leader_board(dataHandler.data)

    cat_agent.save_agent_data(dataHandler.data)
    dataHandler.save_users()

if __name__ == '__main__':
    dataHandler = DataHandler(common.get_data_file_name())
    dataHandler.load_users()

    print("Welcome fellow cat!!! (ฅ^•ﻌ•^ฅ)")
    user_name = input("Enter your code name : ").lower()

    #Easter egg
    if user_name.startswith("bear"):
        print("Sorry! There is nothing here")
    else:
        start_game(dataHandler, user_name)
