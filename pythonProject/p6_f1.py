try:
    print("Start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError):
    print("you have an error")
    print("can't divide by 0")
print("End program")
