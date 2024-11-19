# README python-test-lib

Python Test Library to be used in Python Test APP

## VENV
Poetry

Initialise VENV

```sh
poetry config virtualenvs.in-project true
poetry env use "$(which python3.11)"
```

Stard VENV

```sh
source .venv/bin/activate
```

Install dependencies (after venv activation)
```sh
poetry install
```

## New project

Creates new directory:

```sh
poetry new PROJECT-NAME
```

Inside current directory

```sh
poetry init --name="PROJECT-NAME"
```

## TESTS

```sh
python -m pytest
```

## Install dependencies

### DEV dependencies

```sh
poetry add pytest@latest --dev
poetry add pytest@8.3.3 --dev
```

## Publish

### Build library

Not required if library is distribiuted by git repo. Still, checks if library can be used properly

```sh
poetry build
```