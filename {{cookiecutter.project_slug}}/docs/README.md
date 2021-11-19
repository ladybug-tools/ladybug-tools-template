
## Usage
For generating the documents locally use commands below from the root folder. 

```shell
# install dependencies
cd {{cookiecutter.pkg_name}}
pip install -r dev-requirements.txt

# generate rst files for modules
sphinx-apidoc -f -e -d 4 -o ./docs ./{{cookiecutter.pkg_name}}
# build the documentation under _build/docs folder
sphinx-build -b html ./docs ./docs/_build/docs
```
