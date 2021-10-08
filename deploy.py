import git

repo = git.Repo('.')
repo.git.add('--all')
origin = repo.remote(name='origin')
other = repo.remote(name='other')
origin.push()
other.push()