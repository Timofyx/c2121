def checker(function, *arqs, **kwargs):
    try:
        result = function(*arqs, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
        print(f"No problem. Result - {result}")


def calcute(expression):
    return eval(expression)


checker(calcute, "a+2")
