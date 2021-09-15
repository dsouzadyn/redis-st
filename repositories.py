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