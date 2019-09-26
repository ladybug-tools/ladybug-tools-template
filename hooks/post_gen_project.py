import subprocess

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

git_initialised = initialise_git()
