from colorama import Fore, Style
import colorama
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="cat_life_log.log",filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")



class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 100 # якщо 100% то кіт радісний
        self.hunger = 100 # якщо 100% то кіт наїденний
        self.tired = 0 # якщо 100% то кіт дуже устав
        self.alive = True

    def check_limits(self):
        if self.happiness > 100:
            self.happiness = 100
        if self.happiness < 0:
            self.happiness = 0
        if self.hunger > 100:
            self.hunger = 100
        if self.hunger < 0:
            self.hunger = 0
        if self.tired > 100:
            self.tired = 100
        if self.tired < 0:
            self.tired = 0

    def to_play(self):
        logging.info(f"{self.name} is playing. Hour {hour}. Hunger = {self.hunger}, Happiness = {self.happiness}, Tired = {self.tired}")
        print(Fore.BLUE + "Time to play!" + Style.RESET_ALL)
        self.hunger -= 2
        self.happiness += 5
        self.tired += 5
        self.check_limits()

    def to_sleep(self):
        logging.info(f"{self.name} is sleeping. Hour {hour}. Hunger = {self.hunger}, Happiness = {self.happiness}, Tired = {self.tired}")
        print(Fore.LIGHTGREEN_EX + "Time to sleep!" + Style.RESET_ALL)
        self.happiness += 5
        self.hunger -= 3
        self.tired -= 25
        self.check_limits()

    def to_eat(self):
        logging.info(f"{self.name} is eating. Hour {hour}. Hunger = {self.hunger}, Happiness = {self.happiness}, Tired = {self.tired}")
        print(Fore.LIGHTGREEN_EX + "Eating time!" + Style.RESET_ALL)
        self.tired += 2
        self.hunger += 25
        self.happiness += 10
        self.check_limits()

    def to_walk(self):
        logging.info(f"{self.name} went on a walk. Hour {hour}. Hunger = {self.hunger}, Happiness = {self.happiness}, Tired = {self.tired}")
        print(Fore.BLUE + "Go on a walk" + Style.RESET_ALL)
        self.tired += 3
        self.hunger -= 3
        self.happiness += 2
        self.check_limits()

    def to_be_sad(self):
        logging.info(f"{self.name} has nothing to do. Hour {hour}. Hunger = {self.hunger}, Happiness = {self.happiness}, Tired = {self.tired}")
        print(Fore.RED + "Have nothing to do :(" + Style.RESET_ALL)
        self.tired += 4
        self.hunger -= 3
        self.happiness += 2
        self.check_limits()

    def is_alive(self):
        if self.tired > 100:
            logging.info(f"{self.name} is to tired. Hour {hour}")
            print(Fore.RED + "To tired..." + Style.RESET_ALL)
            self.alive = False
        elif self.happiness <= 0:
            logging.info(f"{self.name} is sad. Hour {hour}")
            print(Fore.RED + "Sadness" + Style.RESET_ALL)
            self.alive = False
        elif self.hunger <= 0:
            logging.info(f"{self.name} had nothing to eat. Hour {hour}")
            print(Fore.RED + "Had Nothing to eat" + Style.RESET_ALL)
            self.alive = False

    def end_of_hour(self):
        print(f"Happiness = {self.happiness}")
        print(f"Hunger = {self.hunger}")
        print(f"Tired = {self.tired}")

    def live(self, Hour):
        Hour = "Hour " + str(Hour) + " of " + self.name + "'s day"
        print(f"{Hour:=^50}")
        live_cube = random.randint(1, 10)
        if live_cube == 1:
            self.to_play()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_walk()
        elif live_cube == 5:
            self.to_be_sad()
        elif live_cube == 6:
            self.to_eat()
        elif live_cube == 7:
            self.to_eat()
        elif live_cube == 8:
            self.to_eat()
        elif live_cube == 9:
            self.to_sleep()
        elif live_cube == 10:
            self.to_sleep()
        self.end_of_hour()
        self.is_alive()


Kuzya_cat = Cat(name="Kuzya")
for hour in range(25):
    if not Kuzya_cat.alive:
        break
    Kuzya_cat.live(hour)