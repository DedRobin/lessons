from create_session import create_current_session
from models import *

session = create_current_session()
query = session.query(User).first()
for x in query.__table__.columns:
    print(x)
print(query.__table__.columns)
