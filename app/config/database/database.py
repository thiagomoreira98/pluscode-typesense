from sqlmodel import SQLModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from app.config.settings import settings

class Database:
    def __init__(self):
        self.engine = create_engine(settings.DATABASE_URL, echo=settings.DATABASE_SHOW_SQL)
        self._session_maker = sessionmaker(bind=self.engine, autoflush=False)

    def init(self):
        SQLModel.metadata.create_all(self.engine)

    @contextmanager
    def get_session(self):
        with self._session_maker() as session:
            try:
                yield session
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
    
database = Database()

