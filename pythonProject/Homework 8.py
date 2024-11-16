import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="sims_log.log",filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

class Human:
    def __init__(self, name='Human', job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()
            logging.warning(f"{self.name} needs to repair the car to get a job.")

    def eat(self):
        logging.info(f"{self.name} wants to eat. Day {day}")
        if self.home.food <= 0:
            logging.warning(f"{self.name} has no food at home! Day {day}")
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                logging.info(f"{self.name} is full. Day {day}")
                return
            self.satiety += 5
            self.home.food -= 5
            logging.info(f"{self.name} ate food. Satiety is now {self.satiety}. Food is now {self.home.food}. Day {day}")

    def work(self):
        logging.info(f"{self.name} is trying to work. Day {day}")
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
            logging.info(f"{self.name} worked and earned {self.job.salary}. Current money: {self.money}. Current satiety: {self.satiety}. Current gladness: {self.gladness}. Day {day}")
        else:
            if self.car.fuel < 20:
                logging.warning(f"{self.name} has low fuel. Buying fuel... Day {day}")
                self.shopping('fuel')

    def shopping(self, manage):
        logging.info(f"{self.name} is shopping for {manage}. Day {day}")
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
                logging.info(f"{self.name} bought fuel for 100$. Day {day}")
                self.money -= 100
                self.car.fuel += 100
            elif manage == 'food':
                print('Yay, I bought food!')
                logging.info(f"{self.name} bought food. Day {day}")
                self.money -= 50
                self.home.food += 50
            elif manage == 'sweets':
                print('Delicious!')
                logging.info(f"{self.name} bought sweets. Day {day}")
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        logging.info(f"{self.name} is repairing the car. Day {day}")
        self.car.strength += 100
        self.money -= 50

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

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            logging.warning(f"{self .name} is in depression. Day {day}")
            return False
        if self.satiety < 0:
            print("Dead...")
            logging.warning(f"{self.name} is dead... Day {day}")
            return False
        if self.money < -500:
            print("Bankrupt")
            logging.warning(f"{self.name} is bankrupt. Day {day}")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            logging.info(f"{self.name} settled in a house.")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
            logging.info(f"{self.name} bought a {self.car.brand}.")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
            logging.info(f"{self.name} got a job as {self.job.job} with salary {self.job.salary}.")
        self.day_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            logging.info(f"{self.name} is going to eat. Day {day}")
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                logging.info(f"{self.name} is cleaning the house. Day {day}")
                print("I don't want, but i will clean the house")
                self.clean_home()
            else:
                logging.info(f"{self.name} is chilling. Day {day}")
                print("Let's chill")
                self.chill()
        elif self.money < 15:
            logging.info(f"{self.name} is going to work. Day {day}")
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            logging.info(f"{self.name} is repairing the car. Day {day}")
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            logging.info(f"{self.name} is chilling. Day {day}")
            print("Let's chill")
            self.chill()
        elif dice == 2:
            logging.info(f"{self.name} is going to work. Day {day}")
            print("Start working")
            self.work()
        elif dice == 3:
            logging.info(f"{self.name} is cleaning the house. Day {day}")
            print("I don't want, but i will clean the house")
            self.clean_home()
        elif dice == 4:
            logging.info(f"{self.name} is going shopping for sweets. Day {day}")
            print("Time to treats")
            self.shopping(manage="sweets")

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