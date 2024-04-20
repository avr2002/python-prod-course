# Python 3.10, match/case statements

name: str = "Peter"

match name:
    case "Peter":
       print("This is an English name.")
    case "Pedro":
        print("This is a Hispanic name.")
    case "पीटर":
        print("This is a Hindi name.")
    case "Питер":
        print("This is a Russian name.")
    case _:
        print("Unknown Origin")
        

def add_numbers(a: float, b: float) -> float:
    return a+b

result = add_numbers(a=1, b=3)


def do_some_math():
    sum = 1+2+3

