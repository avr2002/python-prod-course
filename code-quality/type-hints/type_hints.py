class Duck:
    def __init__(self) -> None: ...

    def __getattr__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


# duck = Duck()


# # no type hinting!!
# duck.quack()
# duck.swim()
# duck.eat()
