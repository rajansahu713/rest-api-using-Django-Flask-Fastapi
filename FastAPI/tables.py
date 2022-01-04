from sqlalchemy import Column, String, Integer
from database import Base



# A SQLAlchemny ORM Place
class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)