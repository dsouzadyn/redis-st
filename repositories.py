import interfaces
import models
import time
import json
import io


class RedisRepository(interfaces.IRedisRepository):
    def __init__(self, redissession) -> None:
        super().__init__()
        self.r = redissession

    def set(self, model: models.RequestModel) -> str:
        ts = str(int(time.time()))
        self.r.set(ts, json.dumps(model.__dict__))
        return ts

    def get(self, key: str) -> models.RequestModel:
        data = json.load(io.BytesIO(self.r.get(key)))
        return models.RequestModel(data['type'], data['body'])

    def remove(self, key: str) -> None:
        self.r.delete(key)


class RedisPubSubRepository(interfaces.IRedisPubSubRepository):
    def __init__(self, redissession):
        super().__init__()
        self.r = redissession
        self.p = redissession.pubsub()

    def publish(self, channel: str, model: models.PubModel) -> str:
        self.r.publish(channel, json.dumps(model.__dict__))
        return "Published {0} to channel {1}".format(json.dumps(model.__dict__), channel)

    def subscribe(self, channel: str) -> str:
        self.p.subscribe(channel)
        return "Subscribed to channel {0}".format(channel)

    def get_data(self, channel: str) -> models.PubModel:
        message = self.p.get_message()
        while (message != None and message['type'] == 'subscribe'):
            message = self.p.get_message()
        data = json.load(io.BytesIO(message['data']))
        return models.PubModel(data['type'], data['body'])
