import git

repo = git.Repo('.')
repo.git.add('--all')
repo.git.commit('-m', 'commit message from python script')
origin = repo.remote(name='origin')
origin.push()

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