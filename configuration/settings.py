from collections.abc import Callable
from typing import Any

from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class SubModel(BaseModel):
    foo: str = 'bar'
    apple: int = 1


class Settings(BaseSettings):
    auth_key: str = ""

    api_key: str = ""

    redis_dsn: RedisDsn = Field(
        'redis://user:pass@localhost:6379/1',
        validation_alias=AliasChoices('service_redis_dsn', 'redis_url'),  
    )
    pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    amqp_dsn: AmqpDsn = 'amqp://user:pass@localhost:5672/'

    special_function: ImportString[Callable[[Any], Any]] = 'math.cos'  

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    model_config = SettingsConfigDict(env_prefix='my_prefix_')  


print(Settings().model_dump())
"""
{
    'auth_key': 'xxx',
    'api_key': 'xxx',
    'redis_dsn': RedisDsn('redis://user:pass@localhost:6379/1'),
    'pg_dsn': PostgresDsn('postgres://user:pass@localhost:5432/foobar'),
    'amqp_dsn': AmqpDsn('amqp://user:pass@localhost:5672/'),
    'special_function': math.cos,
    'domains': set(),
    'more_settings': {'foo': 'bar', 'apple': 1},
}
"""

# export MY_PREFIX_AUTH_KEY="your_auth_key_value"
# export MY_PREFIX_API_KEY="your_api_key_value"
