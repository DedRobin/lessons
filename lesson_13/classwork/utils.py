from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.engine import Engine

DB_USER = "dedrobin"
DB_PASSWORD = "dedrobin"
DB_NAME = "shops"
DB_ECHO = True


def create_db_engine():
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    return engine


def create_db_engine_if_not_exists(engine: Engine) -> None:
    if not database_exists(engine.url):
        create_database(engine.url)
