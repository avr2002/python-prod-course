# Semantic Versioning (SemVer)

Semantic versioning (also known as SemVer) is a versioning system for software releases that aims to provide a standardized way to convey the nature of changes in a software project. It defines a structured format for version numbers and specifies how they should be incremented based on the changes made in a release.

## `<MAJOR>.<MINOR>.<PATCH>`

- `MAJOR` - breaking change, backwards incompatible
- `MINOR` - adding new functionality/feature, backwards compatible
- `PATCH` - bug fixes, performance optimization, backwards compatible

```bash
0.0.0   # Version 0, alpha release(unstable)
0.0.1   # fixing bug
0.0.2
...

0.1.0   # Adding new feature to v0
0.1.1
...

1.0.0   # Major version release v1
1.0.1
```

## Warnings in Newer Versions


- `MAJOR` version changes doesn't remove old feature(s) instantly, instead we `deprecated` the feature and provide long warning period to user using the lastest version of the api that this feature will be removed in the future.



```python
from warnings import warn

def add_number(a: float, b: float) -> float:
    """
    returns sum of two numbers.
    """
    warn(
        message="This is function is deprecated, and will be removed in future versions.",
        category=DeprecationWarning,
        stacklevel=2
    )

    return a + b
```

### What does `stacklevel` do?

The `stacklevel` parameter in Python's `warnings.warn()` function specifies how many levels up the stack frame to issue a warning from. This parameter controls the context in which the warning message appears in the stack trace.

When you issue a warning using `warnings.warn()`, Python captures the current execution context (stack frame) and includes it in the warning message. The `stacklevel` parameter adjusts this context:

- `stacklevel=1` (default): The warning message includes information about the immediate caller of `warnings.warn()`, typically the line where `warn()` is called.
  
- Increasing `stacklevel` by 1 skips one level up the stack frame. For example:
  - `stacklevel=2`: The warning message includes information about the caller of the function that called `warn()`.
  - `stacklevel=3`: The warning message includes information about the caller of the function that called the function that called `warn()`, and so on.

The purpose of `stacklevel` is to provide more context in the warning message about where the deprecated function (`warn()` in this case) is being called from. This can be useful for debugging and understanding the code flow leading up to the deprecated function call.


```python
warn(
    message="This function is deprecated, and will be removed in future versions.",
    category=DeprecationWarning,
    stacklevel=2
)


>>> DeprecationWarning: This is function is deprecated, and will be removed in future versions.
  print(add_number(1, 4))
```
The `stacklevel=2` means that the warning message will indicate the context of the caller of the function that called `warn()`. This helps in identifying the source of the deprecated usage more clearly in the warning message.

>>SOURCE: ChatGPT





## Some articles on SemVer

- [Official SemVer](https://semver.org/)
- [Medium Article](https://medium.com/@TippuFisalSheriff/a-guide-for-android-app-releases-semantic-versioning-2-0-0-cb18526280c9)
- [GFG Article](https://www.geeksforgeeks.org/introduction-semantic-versioning/)
