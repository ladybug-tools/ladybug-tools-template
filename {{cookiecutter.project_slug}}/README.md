[![Build Status](https://travis-ci.org/ladybug-tools/{{cookiecutter.project_slug}}.svg?branch=master)](https://travis-ci.org/ladybug-tools/{{cookiecutter.project_slug}})
[![Coverage Status](https://coveralls.io/repos/github/ladybug-tools/{{cookiecutter.project_slug}}/badge.svg?branch=master)](https://coveralls.io/github/ladybug-tools/{{cookiecutter.project_slug}})

[![Python 2.7](https://img.shields.io/badge/python-2.7-green.svg)](https://www.python.org/downloads/release/python-270/) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# {{cookiecutter.name}}

{{cookiecutter.description}}

## Installation
```console
pip install {{cookiecutter.pypi_name}}
```

## QuickStart
```python
import {{ cookiecutter.pkg_name }}

```

## [API Documentation](http://ladybug-tools.github.io/{{cookiecutter.project_slug}}/docs)

## Local Development
1. Clone this repo locally
```console
git clone git@github.com:ladybug-tools/{{ cookiecutter.project_slug }}

# or

git clone https://github.com/ladybug-tools/{{ cookiecutter.project_slug }}
```
2. Install dependencies:
```console
cd {{ cookiecutter.project_slug }}
pip install -r dev-requirements.txt
pip install -r requirements.txt
```

3. Run Tests:
```console
python -m pytest tests/
```

4. Generate Documentation:
```console
sphinx-apidoc -f -e -d 4 -o ./docs ./{{cookiecutter.pkg_name}}
sphinx-build -b html ./docs ./docs/_build/docs
```
