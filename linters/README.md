
> [Official Course Notes](https://github.com/phitoduck/python-software-development-course)


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
  

# Flake8

- [Docs](https://flake8.pycqa.org/en/latest/)
- [Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)

- Disable Error messages:
  - `flake8 --help`
  
  - Using comments on the line that has error: `# noqa: <Error_Code>`
    - `# noqa: E305`
  
  - Command Line: `flake8 --exclude=<Error_Code(s)> file_name.py`
    - `flake8 --exclude=E305 linting.py`
    - `flake8 --exclude=E4`
    - `flake8 --ignore=E305 linting.py`

- Using VScode `setting.json`

- [Flake8 config file](https://flake8.pycqa.org/en/latest/user/configuration.html)
  - `.flake8` file


- `darglint`: Linting tool that helps doctstrings to match the function signature
  - `darglint linters/linting.py -s=google`
  - [Docs - darglint](https://github.com/terrencepreilly/darglint)
  - [Docs - darglint2](https://github.com/akaihola/darglint2)


# isort

- Managing import statements
- [Docs](https://pycqa.github.io/isort/)
  
  - `isort <file_name.py>`
  - `isort --multi-line VERTICAL_HANGING_INDENT <file_name.py>`: For multi-line imports
  - `isort --multi-line VERTICAL_HANGING_INDENT <file_name.py> --fgw`: Force multi-line imports
  
- [Config-File](https://pycqa.github.io/isort/docs/configuration/config_files.html)
  - `.isort.cfg`

- Configer in VSCode


# Radon

- `pip install radon`

- [Cyclomatic Complexity](https://radon.readthedocs.io/en/latest/intro.html)
  - `radon cc linters/cyclomatic_complexity.py`
  - `radon cc linters/cyclomatic_complexity.py -s`
  - `raw linters/cyclomatic_complexity.py`
  
- [Radon - Flake8](https://radon.readthedocs.io/en/latest/flake8.html)
