import os
from typing import Any, ClassVar, Dict
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_ssm_settings import SsmBaseSettings


class Settings(SsmBaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    region_sqs:str = "eu_central_1"
    bucket=...
    env = ...