from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    GEMINI_API_KEY: str
    # ANTHROPIC_API_KEY: str
    FIREBASE_PROJECT_ID: str

    class Config:
        env_file = ".env"

settings = Settings()