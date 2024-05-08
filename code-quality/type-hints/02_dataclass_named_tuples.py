from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Dict,
    List,
    NamedTuple,
    TypedDict,
    Union,
)

# named tuple from collections
# Point = namedtuple("Point", ['x', 'y'])


# from typing
class Point(NamedTuple):
    x: int
    y: int


point2d = Point(1, 2)
point2d.x
point2d.y


# student: Dict[str, Union[str, int]] = {"name": "Amit", "age": 21}


# bob: "Student"  # works even defined above

# to define class datatypes without quoted like above use from __future__ import annotations
bob: Student


class Student(TypedDict):
    name: str
    age: int
    position: Point
    friends: List["Student"]  # Self-referential type


student: Student = {
    "name": "Amit",
    "age": 21,
    "position": point2d,
    "friends": [{"name": "Mona", "age": 22, "position": Point(2, 1), "friends": []}],
}

# student[] # Now it gives keys as hints for the dictionary
# student["friends"][0]["friends"][0][]


other_student = Student(name="Mona", age=22)
print(other_student)  # prints a dictionary


@dataclass
class NewStudent:
    name: str
    age: int
    position: Point
    friends: List[NewStudent]  # Self-referential type


new_student = NewStudent(
    **{  # type: ignore
        "name": "Amit",
        "age": 21,
        "position": point2d,
        "friends": [
            NewStudent(
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

print(new_student)

# new_student.friends[0].friends[0].friends


# Definining datatypes
TString = str
x: TString = "Namaste Duniya"


TStudentArgsDictKeys = Union[str, int, Point, List[NewStudent]]
TStudentArgsDict = Dict[str, TStudentArgsDictKeys]
