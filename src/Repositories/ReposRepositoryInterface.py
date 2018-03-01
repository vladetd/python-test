import abc

class ReposRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def getRepos():
        pass
