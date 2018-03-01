from ..Repositories.ReposRepositoryInterface import ReposRepositoryInterface

# The repos manager can be injected with any repository
# that implements the Repos repository interface
#
# That means that if in the future repos transfer to bitbucket
# we can just change the implementaion of the repository without
# changing the underlaying logic
class ReposManager:

    reposRepository=None

    def __init__(self, reposInterface: ReposRepositoryInterface):
        self.reposRepository = reposInterface

    def getAllVladetdRepos(self):
        return self.reposRepository.getRepos()
