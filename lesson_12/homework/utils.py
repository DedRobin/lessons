from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists
from platform import system

DB_PATH = Path(__file__).resolve().parent / "shop.sqlite3"
DB_ECHO = False
SYSTEM = system()


def create_db_engine() -> Engine:
    if SYSTEM == "Windows":
        return create_engine(f"sqlite:///{DB_PATH}", echo=DB_ECHO)
    if SYSTEM == "Linux":
        return create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)


def create_db_engine_if_not_exists(engine: Engine) -> None:
    if not database_exists(engine.url):
        create_database(engine.url)
