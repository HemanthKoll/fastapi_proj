from database import engine,Base
from models import User,Order


User.metadata.create_all(bind=engine)
Order.metadata.create_all(bind=engine)
