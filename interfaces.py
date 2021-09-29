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


class IRedisPubSubRepository(abc.ABC):

    @abc.abstractmethod
    def publish(self, channel: str, model: models.PubModel) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def subscribe(self, channel: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self, channel: str) -> models.PubModel:
        raise NotImplementedError
