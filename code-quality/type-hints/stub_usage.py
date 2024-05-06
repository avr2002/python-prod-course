from type_hints import Duck

duck = Duck()

# Now we can get auto completion
duck.quack()

duck.swim()


# Another way of type hinting


def add(
    a,  # type: int
    b,  # type: int
):  # type: (...) -> int
    return a + b


add()  # we can get hints here
