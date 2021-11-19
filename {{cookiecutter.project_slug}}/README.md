[![Build Status](https://github.com/ladybug-tools/{{cookiecutter.project_slug}}/workflows/CI/badge.svg)](https://github.com/ladybug-tools/{{cookiecutter.project_slug}}/actions)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 2.7](https://img.shields.io/badge/python-2.7-green.svg)](https://www.python.org/downloads/release/python-270/) [![IronPython](https://img.shields.io/badge/ironpython-2.7-red.svg)](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.8/)

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
