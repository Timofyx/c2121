import random


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
        print("Time to play!")
        self.hunger -= 2
        self.happiness += 5
        self.tired += 5
        self.check_limits()

    def to_sleep(self):
        print("Time to sleep!")
        self.happiness += 5
        self.hunger -= 3
        self.tired -= 25
        self.check_limits()

    def to_eat(self):
        print("Eating time!")
        self.tired += 2
        self.hunger += 25
        self.happiness += 10
        self.check_limits()

    def to_walk(self):
        print("Go on a walk")
        self.tired += 3
        self.hunger -= 3
        self.happiness += 2
        self.check_limits()

    def to_be_sad(self):
        print("Have nothing to do")
        self.tired += 4
        self.hunger -= 3
        self.happiness += 2
        self.check_limits()

    def is_alive(self):
        if self.tired > 100:
            print("To tired...")
            self.alive = False
        elif self.happiness <= 0:
            print("Sadness")
            self.alive = False
        elif self.hunger <= 0:
            print("Had nothing to eat")
            self.alive = False

    def end_of_day(self):
        print(f"Happiness = {self.happiness}")
        print(f"Hunger = {self.hunger}")
        print(f"Tired = {self.tired}")

    def live(self, Day):
        Day = "Day" + str(Day) + "of" + self.name
        print(f"{Day:=^50}")
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
        self.end_of_day()
        self.is_alive()


Kuzya_cat = Cat(name="Kuzya") # Кузя - це ім'я мого кота =D
for day in range(365):
    if not Kuzya_cat.alive:
        break
    Kuzya_cat.live(day)