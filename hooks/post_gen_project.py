import subprocess
import urllib

INITIALISE_GIT = '{{ cookiecutter.initialise_git }}'
PUSH_TO_GITHUB = '{{ cookiecutter.push_to_github }}'
git_initialised = False

def initialise_git():
    try:
        subprocess.call(["git", "init"])
        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "-m", "\"feat(*): initial commit\""])
        subprocess.call(["git", "tag", "-a", "v{{ cookiecutter.version }}", "-m", "\"initial version\""])
        return True
    except:
        print(
            """
            Failed to initialise the {{cookiecutter.project_slug}} git repo. Please check that you have git installed as a command line tool.
            Then run the following commands:
                git init 
                git add .
                git commit -m "feat(*): initial commit"
                git tag -a v{{cookiecutter.version}} -m "initial version"

            """
        )
        return False

def push_to_github(initialise_git, git_initialised):
    assert initialise_git == 'y', "Cannot push generated repo to github if 'initialise_git' is not 'y'"

    try:
        assert git_initialised
        username = subprocess.check_output(["git", "config", "github.user"])
        token = subprocess.check_output(["git", "config", "github.token"])

        url = "https://{}:{}@api.github.com/orgs/ladybug-tools/repos".format(username, token)
        payload = urllib.urlencode({
            'name': '{{ cookiecutter.project_slug }}',
            'description': '{{ cookiecutter.description }}'
            })

        urllib.urlopen(url, payload)

        subprocess.call(["git", "remote", "add", "origin", "https://github.com/ladybug-tools/{{ cookiecutter.project_slug }}"])
        subprocess.call(["git", "push", "--set-upstream", "origin", "master"])
        return True
    except:
        print(
            """
            Failed to create the {{ cookiecutter.project_slug }} repository on Github. 
            Please visit https://github.com/new and create a repository for ladybug-tools/{{ cookiecutter.project_slug }}.
            You should then be able to run the following commands from the root of the repository:
                git remote add origin https://github.com/ladybug-tools/{{ cookiecutter.project_slug }}
                git push --set-upstream origin master

            """
        )
        return False


if INITIALISE_GIT == 'y':
    git_initialised = initialise_git()

if PUSH_TO_GITHUB == 'y':
    pushed_to_github = push_to_github(INITIALISE_GIT, git_initialised)
