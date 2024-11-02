class Human:
    height = 170
    name = "Vasya"


class Student(Human):
    study = 50


class Worker(Human):
    money = 1000


persona1 = Student()
persona2 = Worker()

print(persona1.height)
print(persona2.height)
print(persona1.study)
print(persona2.money)
