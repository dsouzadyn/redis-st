import redis
import os
from repositories import RedisPubSubRepository, RedisRepository
from models import PubModel, RequestModel
from dotenv import load_dotenv


load_dotenv()


def main():
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'),
        db=os.getenv('REDIS_DB'),
        password=os.getenv('REDIS_PASS'))

    repo = RedisRepository(r)
    pubsub_repo = RedisPubSubRepository(r)
    value = RequestModel('A', 'This is some data')
    repo_value = PubModel('A', 'Test pub sub model')
    key = repo.set(value)
    print(repo.get(key))
    repo.remove(key)
    print(pubsub_repo.subscribe('test_channel'))
    print(pubsub_repo.publish('test_channel', repo_value))
    data = pubsub_repo.get_data('test_channel')
    print(data)


if __name__ == "__main__":
    main()
