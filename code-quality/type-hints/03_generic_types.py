from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Generic,
    List,
    NamedTuple,
    TypeVar,
)

# Generic Types

# TAddableEntity = Union[int, float, str, list, tuple]

# Using TypeVar, enforces that the argument(s) in the function when using
# TAddableEntity as it's datatype take the same datatype
# from the list of given datatpes, which was not the case above using Union
# As shown in below examples
TAddableEntity = TypeVar("TAddableEntity", int, float, str, list, tuple)


def make_list_of_addable_entity(
    a: TAddableEntity, b: TAddableEntity
) -> List[TAddableEntity]:
    return [a, b]


make_list_of_addable_entity(a="hello", b="world")
make_list_of_addable_entity(a=1, b=2)


def add(a: TAddableEntity, b: TAddableEntity) -> TAddableEntity:
    return a + b


add(a=1, b=2)
add("a", "b")

add(a={"a"}, b={"b"})  # wrong, mypy catches it
add(a=1, b="b")  # wrong, mypy catches it


#######

TException = TypeVar("TException", bound=Exception)


# def raise_exception(err: TException):
#     raise err


# More simple way
def raise_exception(err: Exception):
    raise err


raise_exception(Exception("I'm an error"))
raise_exception(ValueError("I'm a value error"))

#########


class Point(NamedTuple):
    x: int
    y: int


point2d = Point(1, 2)


# class LivingOrganism: ...
# class Animal(LivingOrganism): ...
class Animal: ...


# TFriend1 = TypeVar("TFriend1")
# TFriend2 = TypeVar("TFriend2")


# @dataclass
# class Student(Generic[TFriend1, TFriend2]):
#     name: str
#     age: int
#     position: Point
#     friends_type1: List[TFriend1]
#     friends_type2: List[TFriend2]


# student_that_only_likes_animals: Student[Animal, int] = Student(
#     name="Harry",
#     age=12,
#     position=Point(1, 2),
#     friends_type1=[Animal],
#     friends_type2=[1],
# )

# student_that_only_likes_animals.friends_type2[0].


# Can be either "animal" type or "Student" type
TFriend = TypeVar("TFriend", Animal, "Student")


@dataclass
class Student(Generic[TFriend]):
    name: str
    age: int
    position: Point
    friends: List[TFriend]


student_that_only_likes_animals: Student[Animal] = Student(
    name="Harry",
    age=12,
    position=Point(1, 2),
    friends=[Animal()],
)


new_student: Student[Student] = Student(
    **{  # type: ignore
        "name": "Amit",
        "age": 21,
        "position": point2d,
        "friends": [
            Student(
                **{  # type: ignore
                    "name": "Mona",
                    "age": 22,
                    "position": Point(2, 1),
                    "friends": [],
                }
            )
        ],
    }
)
