# README

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
