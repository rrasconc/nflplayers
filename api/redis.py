import redis
from django.conf import settings


redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


def redis_flushall():
    redis_client.flushall()


def redis_get(key):
    """
    Return the value at key name, or None if the key doesn't exist.

    :param str key: Name of the key to retrieve.
    """
    value = redis_client.get(key)
    return value


def redis_set(key, value, ex_seconds):
    """
    Set the value of key name to value that expires in time seconds. time can be represented by an integer or a Python timedelta object.

    :param str key: Name of the key to set.
    :param str value: Value to set.
    :param str ex_seconds: Expiration time in seconds .
    """
    redis_client.setex(name=key, value=value, time=ex_seconds)
