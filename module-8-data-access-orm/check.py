from db.session import SessionLocal
from models.user import User

db = SessionLocal()

users = db.query(User).all()

for u in users:
    print(u.id, u.name)

db.close()
