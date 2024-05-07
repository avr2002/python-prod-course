from typing import Union
from warnings import warn


def add_number(a: float, b: float) -> float:
    """
    returns sum of two numbers.
    """
    warn(
        message="This is function is deprecated, and will be removed in future versions.\n\
                 Use add_numbers() function instead.",
        category=DeprecationWarning,
        stacklevel=2
    )

    return a + b


def add_numbers(*args: Union[int, float]) -> Union[int, float]:
    """Add any number of entered numbers.

    Args:
        args (Union[int, float]): Numbers to be added.

    Returns:
        Union[int, float]: Sum of the numbers.

    Raises:
        TypeError: If any element in args is not int or float.
    """

    # Check if all arguments are either int or float
    if not all(isinstance(num, (int, float)) for num in args):
        raise TypeError("All arguments must be integers or floats")

    # Calculate the sum of numbers
    result = sum(args)
    return result


print(add_number(1, 4))
print(add_numbers(1, 2, 4))
