#!/usr/bin/bash

EXIT_STATUS=0

black --config .black.toml code-quality/type-hints/ || ((EXIT_STATUS++))
pylint --rcfile .pylintrc *.py code-quality/type-hints/*.py || ((EXIT_STATUS++))
flake8 --config .flake8 code-quality/type-hints/ || ((EXIT_STATUS++))
mypy code-quality/type-hints/ --exclude .venv || ((EXIT_STATUS++))
ruff check code-quality/type-hints/ --config ruff.toml --fix || ((EXIT_STATUS++))
isort code-quality/type-hints/ --settings .isort.cfg || ((EXIT_STATUS++))

exit $EXIT_STATUS