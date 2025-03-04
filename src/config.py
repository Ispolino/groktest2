from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str
    debug: bool = True

    CMD_COLOR_CONVERT: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
