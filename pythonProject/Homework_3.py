import random

class Human:
    def __init__(self, name='Human', job=None, car=None, home=None, garden=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.garden = garden

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_garden(self):
        self.garden = HouseGarden()

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping('food')
        else:
            if self.satiety >=100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
            if manage == 'fuel':
                print("I bought fuel! For 100$...")
                self.money -= 100
                self.car.fuel += 100
            elif manage == 'food':
                print('Yay, I bought food!')
                self.money -= 50
                self.home.food += 50
            elif manage == 'sweets':
                print('Delicious!')
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def clean_garden(self):
        self.gladness += 5
        self.garden.flowers = 50
        self.garden.beauty = 100

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def enjoy_garden(self):
        self.gladness += 10
        self.garden.flowers -= 5
        self.garden.beauty -=10

    def day_indexes(self, day):
        day = f" Today is the {day} day of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = f"{self.name}'s indexes"
        print(f"{human_indexes:=^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = f"Home indexes"
        print(f"{home_indexes:=^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:=^50}")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
        garden_indexes = f"Garden indexes"
        print(f"{garden_indexes:=^50}")
        print(f"Garden Flowers - {self.garden.flowers}")
        print(f"Garden Beauty - {self.garden.beauty}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        if self.garden is None:
            self.get_garden()
            print(f"I planted a garden!")
        self.day_indexes(day)
        dice = random.randint(1,6)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I don't want, but i will clean the house")
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money < 15:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("I don't want, but i will clean the house")
            self.clean_home()
        elif dice == 4:
            print("Time to treats")
            self.shopping(manage="sweets")
        elif dice == 5:
            print("Im going to enjoy my garden")
            self.enjoy_garden()
        elif dice == 6:
            print("Im going to clean my garden")
            self.clean_garden()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cant move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class HouseGarden:
    def __init__(self):
        self.flowers = 50
        self.beauty = 100


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1}
}


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}


persona = Human(name='Vasya')

for day in range (1, 8):
    if persona.live(day) == False:
        break