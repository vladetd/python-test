import abc

class APIInterface(abc.ABC):
    @abc.abstractmethod
    def get(self, endpoint, params):
        pass

    @abc.abstractmethod
    def post(self, endpoint, params=None):
        pass

    @abc.abstractmethod
    def delete(self, endpoint, params):
        pass

    @abc.abstractmethod
    def put(self, endpoint, params):
        pass
