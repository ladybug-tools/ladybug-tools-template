# Ladybug Tools Template

Use this repository as a template to write a new modules for Ladybug Tools.

## QuickStart
1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) locally
```console
pip install cookiecutter
```
2. Run cookiecutter against this repository and follow the prompts
```console
cookiecutter gh:ladybug-tools/ladybug-tools-template

# Follow cookiecutter prompts
```

3. If you did not initialise git then do so manually:
```console
git init 
git add .
git commit -m "feat(*): initial commit"
git tag -a v0.0.0 -m "initial version"
```

4. If you did not initialise the project on Github do so manually. Please visit https://github.com/new and create a repository for ladybug-tools/YOUR-PROJECT-SLUG (example: ladybug-tools/fire-ant for a project called Fire Ant).

5. Activate the repository on [TravisCI](https://travis-ci.org/).
  
  ![image](https://user-images.githubusercontent.com/2915573/61428579-bbed0180-a8f0-11e9-8a4e-3ae7816c24a5.png)
  
  and set-up GH_TOKEN and PYPI_PASSWORD.

  ![image](https://user-images.githubusercontent.com/2915573/61428637-0c645f00-a8f1-11e9-9e5a-55b7a71536ed.png)

6. Activate this repository on [coveralls](https://coveralls.io/).

The repository should be ready! Now go write some actual code!