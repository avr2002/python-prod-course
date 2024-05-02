# Pylint

- [Docs](https://pylint.readthedocs.io/en/latest/index.html)

- Run pylint on a file: `pylint file_name.py`
  - Or simply install VScode extenstion  

- Disable message(s) in pylint

```python
from dataclasses import dataclass

# pylint: disable=<message_name/message_id>
# also multiple messages can be disabled, separated by commas.


# pylint: disable=too-many-instance-attributes, C0115
# OR the better way is to specify messages name(s) instead of IDs

# pylint: disable=too-many-instance-attributes, missing-class-docstring
@dataclass
class Book:
    title: str
    num_pages: int
    author: str
    isbn: str
    location_of_writing: str
    genre: str
    rating: float
    weight: int
    price: float
    is_in_series: str
    aaa: int
    aab: int
    aac: int
    aad: int
    aae: int
    aaf: int
```


- Globally disable messages in pylint

  - Can also be done in vscode `settings.json`.
  - By usind pylint command:
  
```bash
pylint --diable <message_name(s)/ID(s)> file_name.py

pylint --disable missing-class-docstring linting.py
```


```bash
pylint --help

  --enable <msg ids>, -e <msg ids>

            Enable the message, report, category or checker with the given id(s). You can either give
            multiple identifier separated by comma (,) or put this option multiple time (only on the command
            line, not in the configuration file where it should appear only once). See also the "--disable"
            option for examples.

  --disable <msg ids>, -d <msg ids>

            Disable the message, report, category or checker with the given id(s). You can either give
            multiple identifiers separated by comma (,) or put this option multiple times (only on the
            command line, not in the configuration file where it should appear only once). You can also use
            "--disable=all" to disable everything first and then re-enable specific checks. For example, if
            you want to run only the similarities checker, you can use "--disable=all
            --enable=similarities". If you want to run only the classes checker, but have no Warning level
            messages displayed, use "--disable=all --enable=classes --disable=W".
```

- Generating `pylint` config file
  - `pylint --generate-rcfile > .pylintrc` 