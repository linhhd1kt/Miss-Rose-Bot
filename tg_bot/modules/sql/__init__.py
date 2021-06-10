from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


# engine = create_engine("mysql://root:root@127.0.0.1/tgbot",encoding='latin1', echo=True)

def start() -> scoped_session:
    engine = create_engine(DB_URI, encoding='utf8')
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
