import redis

class RedisService:
    def __init__(self,host,port,username,password,use_ssl=False):
       self.r = redis.Redis(
            host=host,
            port=port,
            decode_responses=True,
            username=username,
            password=password,
            ssl=use_ssl,
        )

    def get_owner_name(self):
        return self.r.get("owner-name")