#!/usr/bin/env python3
"""Cache class with a decorator to count method calls."""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Use the qualified name of the method as the key
        key = method.__qualname__
        # Increment the count in Redis
        self._redis.incr(key)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Cache with a Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally
        convert it using a provided function.

        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): A callable to convert the
            data back to the desired format.

        Returns:
            Union[str, bytes, int, float, None]:
            The retrieved data, optionally converted.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve a string value from Redis.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Union[str, None]: The retrieved string value or
            None if the key does not exist.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve an integer value from Redis.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Union[int, None]: The retrieved integer value or
            None if the key does not exist.
        """
        return self.get(key, lambda x: int(x))


if __name__ == "__main__":
    cache = Cache()
