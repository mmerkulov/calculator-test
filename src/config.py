from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    WORK_MODE: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
