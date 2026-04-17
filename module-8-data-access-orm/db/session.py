from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,  # muestra SQL en consola (útil para aprender)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
