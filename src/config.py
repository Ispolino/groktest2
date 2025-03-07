from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="TG_",
        env_file_encoding="utf-8",
        extra="allow")


class PostgresqlConfig(BaseSettings):
    host: str
    port: str
    user: str
    password: str
    db_name: str = "users"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
        env_file_encoding="utf-8",
        extra="allow")


class LoggingConfig(BaseSettings):
    debug: bool = True
    cmd_convert_revert: bool = False


class Config(BaseSettings):
    telegram: Settings = Settings()
    db: PostgresqlConfig = PostgresqlConfig()
    logging: LoggingConfig = LoggingConfig()

    @classmethod
    def load(cls) -> "Config":
        return cls()


settings = Config.load()
