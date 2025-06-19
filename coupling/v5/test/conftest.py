from fastapi import FastAPI

from app.core.config import Settings
from app.dependencies import get_settings



@pytest.fixture(scope="session")
def settings() -> Settings:
    settings = get_settings()
    settings.BUCKET = "test-bucket"
    return settings



@pytest_asyncio.fixture()
async def app(settings) -> FastAPI:
    from app.main import app

    def get_settings_override():
        return settings

    app.dependency_overrides[get_settings] = get_settings_override

    yield app

    app.dependency_overrides.clear()
