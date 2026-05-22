import os
import random
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_data_file_name():
    return "user_data.txt"

def get_direction():
    return [[[-1,-1],[-1,0],[0,-1],[0,1],[1,-1],[1,0]], [[-1,0],[-1,1],[0,-1],[0,1],[1,0],[1,1]]]

def get_colour_map():
    return {"B": ["\033[93m", "(ʕ•ᴥ•ʔ)"],
                 "BL": ["\033[93m", "(ʕ•́ᴥ•̀ʔ)"],
                 ".": "\033[34m",
                 "M": "\033[32m",
                 "F": ["\033[31m", "<•))>><"],
                 "#": ["\033[37m", "[#####]"],
                 "R": "\033[0m"}

def get_fish_score(action: str):
    fish_score = {"ABORT": -20, "LOST": -10, "WON": 50, "HIT": 10}
    return fish_score[action]

def game_instructions(agent):
    # https://heartcopypaste.com/cat-ascii-art/
    return f"""\033[92m

      ⠀⠀⠀⠀⠀⡖⢤⡀⠀⠀⣀⣀⣀⣀⡀⠀⠀⢀⡴⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⡇⠀⠙⠚⠉⠉⠀⠀⠀⠉⠉⠓⠋⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Hi agent {agent.agent_name.upper()}, welcome to the clan.
                                             Codename 'IBA' has broken containment unit and is running across the geospatial grid.
           ⡞⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧               If the infiltrator touches the perimeter, our network goes dark.
          ⢹⡷⠦⣤⣀⡀⠀⠀   ⠀⠀⢀⣠⡤⠶⢺⠃⠀⠀⠀⠀⠀        Drop missile payloads to box it in.
         ⢹⠀⠀⣦⠀  ⢹     ⡟   ⣦  ⡟
          ⠈⣇⣀⣠⣬⡅⠀⣠⣴⠿⣄⣀⠀⢬⣤⣀⣀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ The Mission: Input coordinates as x y to drop barriers and trap the bear. 
           ⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Capture before it hits the grid edge and runs. Type ABORT to retreat. 
             ⠙⡶⢤⣀⣀⠀⠀⢀⣀⣠⠤⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⢰⠇⠀⠀⠉⠉⠉⠉⠁⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Fish Points⠀<•))>>< 
             ⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Neutralizing Target: +50pts || Mission Failure : -10pts⠀|| Tactical Retreat: -20pts
            ⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠐⠶⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣸⠀⠀⠀⠀⣤⠀⠀⠀⡄⠀⠀⠀⠀⣷⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⠀⠀Oh, and keep an eye out for on the grid, fish might be drifting through the stream.
            ⣿⠀⠀⠀⠀⣿⠀⠀⠀⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀Blast them, put it in your own pockets (+10pts), HQ doesn't need to know about it.
            ⢹⡀⠀⠀⠀⣿⠀⠀⠀⡇⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠙⠦⣤⣤⣿⣤⣤⣤⣧⣤⣤⣴⣯⣤⣤⣤⣤⡶⠞⠋⠀⠀⠀⠀      Good luck, Agent.
    \033[0m
    """

def game_menu():
    return """ 
        
            1. TRAP THE BEAR IBA! READY AGENT CAT? ฅ(^◕ᴥ◕^)ฅ
            2. FAIL THE MISSION
            3. MISSION INSTRUCTIONS AGAIN?
            4. VIEW YOUR STATS
            5. AGENT LEADER BOARD
            6. CLEAR SCREEN
            
            Hurry Agent!! Enter your choice : """

def coordinate_input():
    attack_words = random.choice(["Ready to engage", "Comms operational", "Calibration complete", "Target ready to lock"])
    return f"""       {attack_words}, Drop the payload at "x y" or "ABORT" and go take a nap: """

def won_lost_banner(outcome: str, agent_name: str):
    banner = ""
    if outcome == "WON":
        banner = f"\n\033[92m MISSION ACCOMPLISHED: Target secure. The Cat Clan honors your service, agent {agent_name}.\033[0m\n"
    elif outcome == "LOST":
        banner = "\n\033[91m MISSION FAILED: The bear Iba slipped through the perimeter. Target lost. Retreat to base immediately.\033[0m\n"
    elif outcome == "ABORT":
        banner = "\n\033[93m MISSION ABORTED: Eject! Eject! Pulling Agent Cat out of the hot zone. Tactically retreating to the shadows.\033[0m\n"
    return banner

def performance_calculator(agent: 'Agent'):
    # Easter egg
    if agent.fish_point > 10000:
        performance = f"DEITY STATUS! The mainframe belongs to you now, Agent {agent.agent_name}."
    elif agent.fish_point > 1000:
        performance = f"Commander Agent {agent.agent_name}! Proud to have you with us."
    elif agent.fish_point > 100:
        performance = "High-value target hunter. Maximum efficiency."
    elif agent.fish_point > 10:
        performance = "Certified Field Agent. Moving up the ranks."
    elif agent.fish_point >= 0:
        performance = "Hope you are a newbie... clean your lenses and try again."
    elif agent.fish_point > -100:
        performance = f"Let's not go there agent {agent.agent_name}.."
    else:
        performance = f"How much is the bear paying you agent {agent.agent_name}?"
    return performance

def agent_status(agent: 'Agent', performance: str):
    return f"""\033[94m
                    .=================================================.
                    |{f"AGENT CAT : {agent.agent_name.upper()}":^49}|
                     =================================================
                     
                     FISH POINTS <•))>>< : {agent.get_fish_point()}
                     
                     SUCCESSFUL OPERATIONS : {agent.get_wins()} WINS
                     
                     PERFORMANCE EVALUATION : {performance}

            \033[0m"""

def print_leaderboard_banner():
    print("\033[32m==================================================================")
    print("                          LEADERBOARD                             ")
    print("==================================================================")
    print("      Agents      |     Fish Points      |   Missions Completed   ")
    print("------------------------------------------------------------------\033[0m")

def wanted_bear(bear_coordinate : tuple):
    trigger_words = random.choice(["You can't catch me","Is that all you got?",
                                   "My kid drops better bombs", "You can't beat me",
                                   "I am inevitable... Sorry thanos", "Ooooh yeahhh!!,"
                                   "I can see my freedom!", "Please stop, I'll pay you with fish ;)",
                                   "Lets team up, we can rule this world", "booo hoooooo"])
    # Source : https://heartcopypaste.com/bear-ascii-art/
    return f"""  
                            ⠛⠛⠛⠛⠛⠛⠛ WANTED BEAR IBA ⠛⠛⠛⠛⠛⠛⠛
                            ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛
                             ⢀⣶⠿⠛⠻⢷⣤⣴⣶⠶⠶⢶⣶⣤⣤⣶⡶⠶⠶⣶⣦⣤⡾⠟⠛⠿⣦⡀⠀
                            ⠀⣾⣧⣾⣿⣷⠄⠉⠁⣀⣀⣀⣀⠀⠉⠉⠀⢀⣀⣀⣀⠈⠉⠠⣾⣿⣷⣼⣷⠀
                            ⠀⢻⣯⣿⡟⠁⠀⠀⠀⠀⠀⠉⠻⣷⣦⣴⣾⠟⠉⠁⠀⠀⠀⠀⠈⢻⣿⣼⡟⠀
                            ⠀⢀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀ ⠈⠻⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠹⣿⡀⠀
                            ⢀⣾⠏⠀⠀⠀⢠⣶⣿⣿⣶⣤⣀⣀⠀⠀⣀⣀⣠⣶⣿⣿⣶⡄⠀⠀⠀ ⠹⣷⡀
                            ⣼⡟⠀⠀⠀⠀⣾⣿⣷⣝⣯⣿⠟⠁⠀⠀⠈⠻⣿⣿⣫⣾⣿⣷⠀⠀⠀⠀⢿⣇
                            ⣿⡇⣤⠀⠀⠀⠸⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠇⠀⠀⠀⣤⢸⣿
                            ⣿⣿⣿⠀⠀⠀⠀⠈⠉⣹⣿⠀⠀⣠⣤⣤⣄⡀⠀⣿⣏⠉⠁⠀⠀⠀⢀⣿⣿⣿
                            ⠀⢻⣿⣿⣆⠀⢀⠀⠀⣿⡇⠀⠀⠻⢿⡿⠟⠀⠀⢸⣿⠀⠀⡀⠀⣰⣿⣿⡟⠀
                            ⠀⠈⢿⠻⣿⣧⣸⣦⠀⢿⣿⣤⢴⡶⠾⠷⢶⡦⣤⣾⡿⠀⣴⣇⣼⣿⠟⡿⠁ {trigger_words}
                            ⠀⠀⠀⠀⠙⢿⣿⣿⣷⣼⣿⣿⡷⢭⣭⣭⡭⢶⣿⣿⣧⣾⣿⣿⡿⠋⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠈⠻⣿⣿⣿⣿⠟⠁⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
                            ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛
                         GEOSPATIAL LOCATIONS DETECTED ⌖ AT {bear_coordinate}
                    """

def jailed_bear():
    surrender_words = random.choice(["NO!!!!! CURSE YOU AGENT!","AHHH, NOT AGAIN",
                                     "SORRY MOM, I MESSED UP AGAIN", "OOOH OOHH",
                                     "DAMNNN YOUU AGENT", "IF YOU LET ME GO, I WILL MAKE YOU RICH",
                                     "NOOOOOOOOOOOOOOOOOOOOO", "ALL BEARS ASSEMBLE.. AH NEVER MIND",
                                     "DON'T TORTURE ME", "WHAT ARE YOU GOING TO DO TO ME?"])
    return f"""
                    ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛
                    ||⠛⠛⠛⠛⠛⠛||⠛⠛⠛⠛⠛||⠛⠛⠛⠛||⠛⠛⠛⠛||⠛⠛⠛⠛||
                    || ⢀⣶⠿⠛⠻||⣤⣴⣶⠶⠶||⣤⣤⣶⡶||⣶⣦⣤⡾||⠿⣦⡀⠀||
                    ||⠀⣾⣧⣾⣿⣷||⠉⠁⣀⣀⣀||⠉⠉⠀⢀||⣀⠈⠉⠠||⣷⣼⣷⠀||
                    ||⠀⢻⣯⣿⡟⠁||⠀⠀⠀⠀⠉||⣦⣴⣾⠟||⠀⠀⠀⠀||⣿⣼⡟⠀||
                    ||⠀⢀⣿⠏⠀⠀||⠀⠀⠀⠀⠀||⠻⡿⠁⠀||⠀⠀⠀⠀||  ⠹⣿||⠀
                    ||⢀⣾⠏⠀⠀⠀||⣶⣿⣿⣶⣤||⠀⠀⣀⣀||⣿⣿⣶⡄||⠀ ⠹⣷||
                    ||⣼⡟⠀⠀⠀⠀||⣿⣷⣝⣯⣿||⠀⠀⠈⠻||⣫⣾⣿⣷||⠀⠀⢿⣇||
                    ||⣿⡇⣤⠀⠀⠀||⣿⣿⣿⣿⡏||⠀⠀⠀⠀||⣿⣿⣿⠇||⠀⣤⢸⣿||
                    ||⣿⣿⣿⠀⠀⠀||⠈⠉⣹⣿⠀||⣤⣤⣄⡀||⣏⠉⠁⠀||⢀⣿⣿⣿||
                    ||⠀⢻⣿⣿⣆⠀||⠀⠀⣿⡇⠀||⢿⡿⠟⠀||⣿⠀⠀⡀||⣿⣿⡟⠀||
                    ||⠀⠈⢿⠻⣿⣧||⣦⠀⢿⣿⣤||⠾⠷⢶⡦||⡿⠀⣴⣇||⠟⡿⠁⠀||
                    ||⠀⠀⠀⠀⠙⢿||⣿⣷⣼⣿⣿||⣭⣭⡭⢶||⣧⣾⣿⣿||⠀⠀{surrender_words}
                    ||⠀⠀⠀⠀⠀⠀||⠀⠀⠈⠛⠈||⣿⣿⣿⠟||⠁⠀⠀⠀||⠀⠀⠀⠀||
                    ||⣶⣶⣶⣶⣶⣶||⣶⣶⣶⣶⣶||⣿⣿⣷⣶||⣶⣶⣶⣶||⣶⣶⣶⣶||
                    ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛
            """

def bear_free():
    return f"""
                .===============================================.
                |          FAILURE: GEOLOCATION UNKNOWN         |
                |===============================================|
                |                                               |
                |          STATUS:      BEAR IBA ESCAPED        |
                |       SATELLITE RADAR:   OFFLINE              |
                |                                               |
                |  ENEMY UNIT HAS SLIPPED INTO THE BLIND SPOT   |
                |                                               |
                |          MISSION FAILED!! ₍˄- ˕ -˄₎           |
                |     CAT SATELLITE OVERRIDE: INITIATED...      |
                |                                               |                                                                                   I AM FREE!!...
                '==============================================='
            """

def exit_game_print():
    print("            This game will self destruct in 5 seconds")
    for i in range(5, 0, -1):
        print(f"\033[31m                             {i}{'.' * 3}\033[0m")
        time.sleep(1)
    #Easter egg
    print("""\033[31m
                        _.-^^---....,,-- 
                _---      -      -      --_ A_P
               <        -                >
                < |    ^^        -    ^^     -R 
                \\._-    -     -        T _./ 
                   ```--. . , ; .--'''
                    ^^   )  ;   (       -
                      E  .-| | |=-.
                    `-=#$%&%$@#$$#@# =-'
                   B     ; : |  ; 
               _____.,-#%&$@%$%&%$#~,._AR____
              _                       _
    \033[0m""")

def funny_exception():
    matrix = """
                            The missile tears through the green code of the grid.
                            A voice whispers from a nearby payphone: Wake up, Neo!"""

    marvel = """
                            Your missile slipped through a dimensional rift.
                            A deep, echoing voice booms back from the cosmos: Bring it on, I can do this all day"""

    mission_impossible = """
                            Your missile flew completely off the tactical satellite map.
                            Benji cracks through your earpiece: 'Uh, Agent Cat? Ethan is hanging off a plane
                            down there and you just nearly clipped him"""

    harry_potter = """
                            Your missile took a wrong turn at Diagon Alley.
                            It's Levi-O-sa, not launch-a-missile-into-the-Forbidden-Forest!"""
    f1 = """
                            Missile trajectory exceeded track limits at Turn 1.
                            Your race engineer screams over the team radio: 'Box, box!"""
    naruto = """
                            Your missile missed the grid and flew past the Hidden Leaf.
                            Madara laughs maniacally from the shadows: You lack hatred, Agent Cat... and tracking skills."""

    dbz = """
                            You charged that missile for 5 episodes just to overshoot the map!
                            You destroyed planet Namek, hopefully Goku escaped in time."""

    exception_message = [matrix, marvel, mission_impossible, harry_potter, f1, naruto, dbz]
    return random.choice(exception_message)