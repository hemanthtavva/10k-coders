from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/electronics_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflus = False,
    bind = engine
)

base = declarative_base()