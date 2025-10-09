# db.py
from sqlmodel import SQLModel, create_engine, Session, text
from config import settings
import os

# ensure data directory
os.makedirs(os.path.dirname(settings.DATABASE_URL.replace("sqlite:///", "")), exist_ok=True)

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)

def init_db():
    # SQLModel tables
    SQLModel.metadata.create_all(engine)
    # SQLite pragmas
    with Session(engine) as session:
        session.exec(text("PRAGMA journal_mode=WAL;"))
        session.exec(text("PRAGMA foreign_keys=ON;"))
        #
        session.exec(text("PRAGMA synchronous=NORMAL;"))
        session.commit()
def get_session():
    with Session(engine) as session:
        yield session
