from git import Repo
import os

# os.chdir('./align')
# print(os.getcwd())
PATH_OF_GIT_REPO = '.'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

git_push()

# import git

# repo = git.Repo('.')
# repo.git.add('--all')
# repo.git.commit('-m', 'commit message from python script')
# origin = repo.remote(name='origin')
# origin.push()

# os.chdir('./align')
# Get the current working directory
# cwd = os.getcwd()

# Print the current working directory
# print("Current working directory: {0}".format(cwd))
# repo = Repo(cwd)
# repo.git.add('--all')
# repo.git.commit('-m', 'commit message from python script')
# origin = repo.remote(name='origin')
# origin.push()