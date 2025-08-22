from pathlib import Path


class Settings:
    # path to data folder with db using path for config.py
    DB_DIR = Path(__file__).resolve().parent.parent.parent / "data"
    # create folder if not already
    DB_DIR.mkdir(parents=True, exist_ok=True)
    # join paths
    DATABASE_URL = f"sqlite:///{DB_DIR / 'db.sqlite3'}"


settings = Settings()
