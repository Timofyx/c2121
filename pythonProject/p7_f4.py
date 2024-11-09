def checker(function, *arqs, **kwargs):
    try:
        result = function(*arqs, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
        print(f"No problem. Result - {result}")



@checker
def calculate(expression):
    return eval(expression)



checker("2/0")
