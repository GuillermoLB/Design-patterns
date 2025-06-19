from functools import lru_cache
import logging
from typing import Annotated, Any

from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordBearer

from src.core.config import Settings


import boto3

from src.models.usuario.usuario_model import UsuarioModel
from src.services.auth.auth_refresh_service import AuthRefreshService

auth_service = AuthRefreshService() # NOTE: If it was declaratively defined, we wouldn't have to initialize it here (with "pseudo-hard-coded parameters")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

logger = logging.getLogger(__name__)

@lru_cache
def get_settings():
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)] # So in routes we can use settings: UserDep instead of settings: Settings = Depends(get_settings) -> DRY principle
