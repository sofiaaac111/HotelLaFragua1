from pydantic_settings import BaseSettings

class Config(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_DB: str

    class Config:
        env_file = ".env"
        extra = "allow"
