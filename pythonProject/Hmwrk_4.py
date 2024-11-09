import random

class GameConsole:
    def __init__(self, name, brand, model, storage, games, game_sizes):
        self.name = name
        self.brand = brand
        self.model = model
        self.storage = storage
        self.installed_games = []
        self.network_connected = False
        self.games = games
        self.game_sizes = game_sizes

    def install_game(self, game_name):
        game_size = self.game_sizes[game_name]
        if self.storage >= game_size:
            self.installed_games.append(game_name)
            self.storage -= game_size
            print(f"{game_name} встановлено на {self.model}. Залишилось {self.storage} GB вільного місця.")
        else:
            print(f"Недостатньо місця для встановлення {game_name} на {self.model}.")

    def remove_game(self, game_name):
        game_size = self.game_sizes[game_name]
        if game_name in self.installed_games:
            self.installed_games.remove(game_name)
            self.storage += game_size
            print(f"{game_name} видалено з {self.model}. Залишилось {self.storage} GB вільного місця.")
        else:
            print(f"{game_name} не знайдено на {self.model}.")

    def connect_network(self):
        self.network_connected = True
        print(f"{self.model} підключено до мережі.")

    def update_system(self):
        if self.network_connected:
            print(f"Оновлення системи {self.model}...")
            print(f"Система {self.model} оновлена до останньої версії.")
        else:
            print(f"Не вдається оновити систему {self.model}. Підключіться до інтернету.")

    def play_game(self, game_name):
        if game_name in self.installed_games:
            if random.random() < 0.2:
                print(f"{self.model} треба оновити, щоб змогти грати в {game_name}.")
                self.update_system()
            print(f"Запуск {game_name}...")
        else:
            print(f"{game_name} не встановлено на {self.model}.")

    def day_indexes(self, day):
        day_info = f" Володів {self.name} {day} дні"
        print(f"{day_info:=^50}", "\n")
        console_indexes = f"{self.name}"
        print(f"{console_indexes:=^50}", "\n")
        print(f"Пам'ять - {self.storage}GB")
        print(f"Встановленні ігри - {self.installed_games}")
        print(f"Підключення до інтернету - {self.network_connected}")

    def consoleDay(self, day):
        self.day_indexes(day)
        if not self.network_connected:
            self.connect_network()
        dice = random.randint(1, 4)
        if dice == 1:
            game = random.choice(self.games)
            self.install_game(game)
        elif dice == 2:
            if self.installed_games:
                game = random.choice(self.installed_games)
                self.remove_game(game)
            else:
                print("Немає встановлених ігор для видалення.")
        elif dice == 3:
            if self.installed_games:
                game = random.choice(self.installed_games)
                self.play_game(game)
            else:
                print("Немає встановлених ігор для запуску.")
        elif dice == 4:
            self.update_system()

class NintendoSwitch(GameConsole):
    def __init__(self, model, storage):
        games = ["The Legend of Zelda", "Super Mario Odyssey", "Splatoon 3", "Metal Gear Solid 3"]
        game_sizes = {"The Legend of Zelda": 15, "Super Mario Odyssey": 6, "Splatoon 3": 10, "Metal Gear Solid 3":5}
        super().__init__("Nintendo Switch", "Nintendo", model, storage, games, game_sizes)

class PlayStation5(GameConsole):
    def __init__(self, model, storage):
        games = ["God of War: Ragnarok", "Ratchet & Clank", "Spider-Man: Miles Morales", "Metal Gear Solid V"]
        game_sizes = {"God of War: Ragnarok": 100, "Ratchet & Clank": 20, "Spider-Man: Miles Morales": 70, "Metal Gear Solid V":30}
        super().__init__("PlayStation 5", "Sony", model, storage, games, game_sizes)

class PlayStationPortable(GameConsole):
    def __init__(self, model, storage):
        games = ["God of War", "Gran Turismo", "Metal Gear Solid: Peace Walker", "Persona 3 Portable"]
        game_sizes = {"God of War": 1, "Gran Turismo": 2, "Metal Gear Solid: Peace Walker": 2, "Persona 3 Portable": 2}
        super().__init__("PSP", "Sony", model, storage, games, game_sizes)

class Xbox(GameConsole):
    def __init__(self, model, storage):
        games = ["Halo Infinite", "Forza Horizon 5", "Microsoft Flight Simulator", "Metal Gear Solid V"]
        game_sizes = {"Halo Infinite": 30, "Forza Horizon 5": 50, "Microsoft Flight Simulator": 100, "Metal Gear Solid V":30}
        super().__init__("Xbox Series S", "Microsoft", model, storage, games, game_sizes)

    console_list = {
        "Nintendo Switch": {"brand": "Nintendo", "model": "Switch", "storage": 32,
                            "games": ["The Legend of Zelda", "Super Mario Odyssey", "Splatoon 3", "Metal Gear Solid 3"],
                            "game_sizes": {"The Legend of Zelda": 15, "Super Mario Odyssey": 6, "Splatoon 3": 10, "Metal Gear Solid 3":5}},
        "PlayStation Portable": {"brand": "Sony", "model": "PSP", "storage": 16,
                              "games": ["God of War", "Gran Turismo", "Metal Gear Solid: Peace Walker", "Persona 3 Portable"],
                              "game_sizes": {"God of War": 1, "Gran Turismo": 2, "Metal Gear Solid: Peace Walker": 2, "Persona 3 Portable":2}},
        "PlayStation 5": {"brand": "Sony", "model": "PS5", "storage": 825,
                          "games": ["God of War: Ragnarok", "Ratchet & Clank", "Spider-Man: Miles Morales", "Metal Gear Solid V"],
                          "game_sizes": {"God of War: Ragnarok": 100, "Ratchet & Clank": 20, "Spider-Man: Miles Morales": 70, "Metal Gear Solid V":30}},
        "Xbox Series S": {"brand": "Microsoft", "model": "Series S", "storage": 512,
                          "games": ["Halo Infinite", "Forza Horizon 5", "Microsoft Flight Simulator", "Metal Gear Solid V"],
                          "game_sizes": {"Halo Infinite": 30, "Forza Horizon 5": 50, "Microsoft Flight Simulator": 100, "Metal Gear Solid V":30}}
    }

    def create_console(console_list):
        console_name = random.choice(list(console_list.keys()))
        console_info = console_list[console_name]
        return GameConsole(console_name, console_info["brand"], console_info["model"], console_info["storage"],
                           console_info["games"], console_info["game_sizes"])

    console = create_console(console_list)
    for day in range(1, 10):
        console.consoleDay(day)