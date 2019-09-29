# Ladybug Tools Template

Use this repository as a template to write a new modules for Ladybug Tools.

## QuickStart
1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) and [pygithub](https://pygithub.readthedocs.io/en/latest/introduction.html) (to automate creating the repositories on Github after generating them locally)
```console
pip install cookiecutter pygithub
```
2. Run cookiecutter against this repository and follow the prompts
```console
cookiecutter gh:ladybug-tools/ladybug-tools-template

# Follow cookiecutter prompts
```

3. If you did not initialise the project on Github do so manually. Please visit https://github.com/new and create a repository for ladybug-tools/YOUR-PROJECT-SLUG (example: ladybug-tools/fire-ant for a project called Fire Ant). If you don't have the correct authorization to create repositories on the ladybug-tools organization then create a repo for your Github user and get in touch with the admins.

4. Activate the repository on [TravisCI](https://travis-ci.org/).

  ![image](https://user-images.githubusercontent.com/2915573/61428579-bbed0180-a8f0-11e9-8a4e-3ae7816c24a5.png)

  and set-up `GH_TOKEN` and `PYPI_PASSWORD`.

  ![image](https://user-images.githubusercontent.com/2915573/61428637-0c645f00-a8f1-11e9-9e5a-55b7a71536ed.png)

5. Activate this repository on [coveralls](https://coveralls.io/) by going to "ADD REPOS"
at the menu on the left-hand side at the link. Note that you will also likely want to set
the "Coverage Decrease Failure Threshold" of the repo to be something like 1% since the
default (0%) often causes build failure messages for small tweaks that don't require new
tests. To change the coverage decrease failure threshold, you can follow the instructions
[here](https://github.com/deepchem/deepchem/issues/648).

The repository should be ready! Now go write some actual code!
