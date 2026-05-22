class DataHandler:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = {}

    def load_users(self):
        try:
            with open(self.file_name, "r") as f:
                for line in f.readlines():
                    username, fish_point, wins = line.strip().split(",")
                    self.data[username] = {"fish_point" : int(fish_point.strip()), "wins" : int(wins.strip())}
        except FileNotFoundError:
            print("Cat clan is in trouble, I think bear destroyed our system file!")
        except (ValueError, IndexError) :
            print("I'M PANICKING!!! OUR SYSTEM IS CORRUPTED")

    def save_users(self):
        with open(self.file_name, "w") as f:
            for key in self.data:
                f.write(f"{key}, {self.data[key]['fish_point']}, {self.data[key]['wins']} \n")

    def get_data(self):
        return self.data