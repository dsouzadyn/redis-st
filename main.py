import redis
import os
from repositories import RedisRepository
from models import RequestModel
from dotenv import load_dotenv


load_dotenv()

def main():    
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'), 
        port=os.getenv('REDIS_PORT'), 
        db=os.getenv('REDIS_DB'),
        password=os.getenv('REDIS_PASS'))

    repo = RedisRepository(r)
    value = RequestModel('A', 'This is some data')
    key = repo.set(value)
    print(repo.get(key))
    repo.remove(key)


if __name__ == "__main__":
    main()
