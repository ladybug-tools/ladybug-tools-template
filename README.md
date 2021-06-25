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

3. Because Github Actions and cookiecutter both use `{{` and `}}` to denote text that
should be replaced, you must go through the `ci.yaml` file after running cookiecutter
and manually replace all instances of `[[` with `{{` and `]]` with `}}`.

4. If you did not initialize the project on Github do so manually. Please visit https://github.com/new and create a repository for ladybug-tools/YOUR-PROJECT-SLUG (example: ladybug-tools/fire-ant for a project called Fire Ant). If you don't have the correct authorization to create repositories on the ladybug-tools organization then create a repo for your Github user and get in touch with the admins.

5. Add `GH_TOKEN`, `PYPI_USERNAME` and `PYPI_PASSWORD` to project secrets on GitHub.
  The secrets are set in Ladybug Tools organization level.

  ![image](https://user-images.githubusercontent.com/2915573/101363031-dc638600-386e-11eb-9042-600ee03e300f.png)

65. Activate this repository on [coveralls](https://coveralls.io/) by going to "ADD REPOS"
at the menu on the left-hand side at the link. Note that you will also likely want to set
the "Coverage Decrease Failure Threshold" of the repo to be something like 1% since the
default (0%) often causes build failure messages for small tweaks that don't require new
tests. To change the coverage decrease failure threshold, you can follow the instructions
[here](https://github.com/deepchem/deepchem/issues/648).

The repository should be ready! Now go write some actual code!
