from .ReposRepositoryInterface import ReposRepositoryInterface
from ..APIs.GithubAPI import GithubAPI
from ..Mappers.GithubRepoMapper import GithubRepoMapper

# Github repository consisting of methods for communication with
# the Github api implemented in APIs/GithubAPI
class GithubApiRepository(ReposRepositoryInterface):

    api=None

    def __init__(self):
        self.api = GithubAPI()

    def getRepos(self):
        data = self.api.get('users/vladetd/repos')
        mapper = GithubRepoMapper()

        result = []
        for repo in data:
            mappedRepo = mapper.map(repo)
            result.append(mappedRepo)

        return result
