import redis
import os
from dotenv import load_dotenv


load_dotenv()

def main():    
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'), 
        port=os.getenv('REDIS_PORT'), 
        db=os.getenv('REDIS_DB'),
        password=os.getenv('REDIS_PASS'))
    r.set('foo', 'bar')
    foo = r.get('foo')
    print(foo)

if __name__ == "__main__":
    main()
