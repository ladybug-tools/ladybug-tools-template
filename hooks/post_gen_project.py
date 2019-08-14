import subprocess
from github import Github

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

def push_to_github(git_initialised):
    try:
        assert git_initialised
        username = subprocess.check_output(
            ["git", "config", "github.user"]).decode("utf-8")[:-1]
        token = subprocess.check_output(
            ["git", "config", "github.token"]).decode("utf-8")[:-1]


        payload = {
            'name': '{{ cookiecutter.project_slug }}',
            'description': '{{ cookiecutter.description }}'
            }

        g = Github(username, token)

        org = g.get_organization('ladybug-tools')

        org.create_repo(
            name='{{ cookiecutter.project_slug }}',
            description='{{ cookiecutter.description }}'
            )


        subprocess.call(["git", "remote", "add", "origin", "https://github.com/ladybug-tools/{{ cookiecutter.project_slug }}"])
        subprocess.call(["git", "push", "--set-upstream", "origin", "master"])
        return True
    except Exception as e:
        print('')
        print(e)
        
        print(
            """
Failed to create the {{ cookiecutter.project_slug }} repository on Github. 
Please visit https://github.com/new and create a repository for ladybug-tools/{{ cookiecutter.project_slug }}.
If you don't have the right Authorization to create a repo in the ladybug-tools org then just create it for your Github
Account and get in touch with the ladybug-tools admins.
You should then be able to run the following commands from the root of the repository:
    
    git remote add origin https://github.com/ladybug-tools/{{ cookiecutter.project_slug }}
    # or
    git remote add origin https://github.com/<YOUR-USERNAME>/{{ cookiecutter.project_slug }}


    git push --set-upstream origin master

            """
        )

        return False


git_initialised = initialise_git()

if PUSH_TO_GITHUB == 'yes':
    pushed_to_github = push_to_github(git_initialised)
