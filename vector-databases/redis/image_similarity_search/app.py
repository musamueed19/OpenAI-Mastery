import os
from dotenv import load_dotenv

load_dotenv()

from redis_service import RedisService

def main():
    use_ssl = os.getenv("REDIS_SSL", "true").strip().lower() in ("1", "true", "yes", "on")
    redis_client = RedisService(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        username=os.getenv('REDIS_USERNAME'),
        password=os.getenv('REDIS_PASSWORD'),
        use_ssl=use_ssl,
    )
    
    owner_name = redis_client.get_owner_name()
    print(f"Owner Name: {owner_name}")



if __name__ == "__main__":
    main()