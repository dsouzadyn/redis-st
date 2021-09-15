import abc
import models

class IRedisRepository(abc.ABC):

    @abc.abstractmethod
    def set(self, model: models.RequestModel) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, key: str) -> models.RequestModel:
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, key: str) -> None:
        raise NotImplementedError
