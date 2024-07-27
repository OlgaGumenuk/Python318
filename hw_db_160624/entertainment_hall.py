from hw_db_160624.databasehw import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Entertainment_hall(Base):
    __tablename__ = 'entertainment_hall'

    id = Column(Integer, primary_key=True)
    hall = Column(String(100), nullable=False)
    readers = relationship("Readers")

    def __repr__(self):
        return f"Зал (ID: {self.id}, Наименование: {self.hall})"
