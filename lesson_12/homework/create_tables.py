from sqlalchemy.orm import sessionmaker
from models import Base, User, Product, Purchase
from utils import create_db_engine, create_db_engine_if_not_exists

engine = create_db_engine()
create_db_engine_if_not_exists(engine=engine)

Base.metadata.create_all(engine)
CurrentSession = sessionmaker(bind=engine)
current_session = CurrentSession()
