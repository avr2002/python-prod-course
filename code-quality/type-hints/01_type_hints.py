class Duck:
    def __init__(self) -> None: ...

    def __getattr__(self, attr):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


duck = Duck()


# no type hinting!!
duck.quack()

duck.swim()

duck.eat()


var: int = 1
var = "hi"  # mypy error


def consume_many_types(
    num: int,
    decimal: float,
    boolean: bool,
    string: str,
    binary=bytes,
    obj=object,
) -> None: ...


from typing import (
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)

nums: list[int] = []  # introduced in python 3.9
backward_compatible_nums: List[int] = []

three_dimensional_vector: tuple[int, int, int] = (1, 1, 1)
new_three_dimensional_vector: Tuple[int, float, str] = (1, 2.0, "3")


n_d_vectors: Tuple[float, ...] = 1, 2, 3, 4, 5

students_to_ages: Dict[str, int] = {
    "bobby": 25,
    "murph": 27,
    "alice": 21,
}

fruits: Set[str] = {"apple", "kiwi", "banana"}


class Animal: ...


x = Animal
gecko = x()


miscellaneous_values: List[Union[int, float, str, Type]] = [
    1,
    1.0,
    "hi",
    object,
    "hi",
    2,
    list,
]

# for newer python versions, we can do like this to
x: int | float | str | Type
x = "hi"

new_miscellaneous_values: List[int | float | str | Type] = [
    1,
    1.0,
    "hi",
    object,
    "hi",
    2,
    list,
]


# pre-Python 3.10
maybe_num: Optional[int] = None
maybe_num = 1

# OR

maybe_num: Union[int, None] = None
maybe_num = 1

# Python 3.10+
maybe_num: int | None = None
maybe_num = 1


x: Optional[int] = None


def greet(name: Optional[str] = None) -> None:
    if not name:
        print("Hello")
        return
    print(f"Hello, {name}!")
