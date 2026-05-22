import common

class CatAgent:
    def __init__(self, username: str):
        self.agent_name = username
        self.wins = 0
        self.fish_point = 0

    def load_agent(self, data: dict):
        if self.agent_name in data:
            agent_details = data[self.agent_name]
            self.fish_point = agent_details["fish_point"]
            self.wins = agent_details["wins"]
            return False
        return True

    def save_agent_data(self, data: dict):
        data[self.agent_name] = {"fish_point": self.get_fish_point(), "wins": self.get_wins()}

    def set_fish_point(self, fish_point):
        self.fish_point += fish_point

    def set_wins(self):
        self.wins += 1

    def get_fish_point(self):
        return self.fish_point

    def get_wins(self):
        return self.wins

    def agent_stats(self):
        performance = common.performance_calculator(self)
        return common.agent_status(self, performance)


    def show_leader_board(self, data: dict):
        self.save_agent_data(data)
        sorted_data = dict(sorted(
            data.items(),
            key=lambda item: (item[1]['fish_point'], item[1]['wins']),
            reverse=True
        ))

        common.print_leaderboard_banner()
        for key, value in sorted_data.items():
            if key == self.agent_name:
                print(f"\033[92m{key:^18}| {value['fish_point']:^22}| {value['wins']:^22}\033[0m")
            else:
                print(f"{key:^18}| {value['fish_point']:^22}| {value['wins']:^22}")