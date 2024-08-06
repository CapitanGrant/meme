from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MINIO_ENDPOINT: str = 'localhost:9000'
    MINIO_ACCESS_KEY: str = 'minioadmin'
    MINIO_SECRET_KEY: str = 'minioadmin'
    MINIO_BUCKET: str = 'memes'
    DATABASE_URL: str = 'sqlite:///./test.db'
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    class Config:
        from_attributes = True


settings = Settings()

