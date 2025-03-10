from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEVELOP: bool = False
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8900
    TITLE: str = 'API'
    VERSION: str = 'v1.0'
    DOC_URL: str = '/docs'
    OPENAPI_URL: str = '/openapi.json'
    LOG_LEVEL: str = 'debug'
    LOG_FORMAT: str = (
        '{"time": "%(asctime)s", "level": "%(levelname)s", "file": "%(name)s", "line": "%(lineno)s", "msg": "%(msg)s"}'
    )
    WORKERS: int = 1


settings = Settings(
    _env_file='./../.env',
    _env_file_encoding='utf-8',
)
