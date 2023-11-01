import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    db_url = os.environ.get("POSTGRES_DSN")


settings = Settings()
