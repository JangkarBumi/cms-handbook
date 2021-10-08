import git

repo = git.Repo('.')
repo.git.add('--all')
origin = repo.remote(name='origin')
origin.push()