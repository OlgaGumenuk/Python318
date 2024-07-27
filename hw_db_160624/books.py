from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from hw_db_160624.databasehw import Base

parts_table = Table('parts', Base.metadata,
                    Column('group_id', Integer, ForeignKey('books.id')),
                    Column('hall.id', Integer, ForeignKey('entertainment_hall.id'))
                    )


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name_b = Column(String(100), nullable=False)
    entertainment_hall = relationship("Books", secondary=parts_table, backref='entertainment_hall_books')

    def __repr__(self):
        return f"Книга (ID: {self.id}, Название: {self.name_b})"


