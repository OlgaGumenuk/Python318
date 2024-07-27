from sqlalchemy import Column, Integer, String, ForeignKey

from hw_db_160624.databasehw import Base


class Readers(Base):
    __tablename__ = 'readers'

    id = Column(Integer, primary_key=True)
    surname = Column(String(200), nullable=False)
    name = Column(String(200), nullable=False)
    patronymic = Column(String(200), nullable=False)
    born = Column(Integer, nullable=False)
    hall = Column(String(200), ForeignKey('hall.id'))

    def __init__(self, full_name, born, id_hall):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.born = born
        self.hall = id_hall


    def __repr__(self):
        return f"Читатель (ФИО: {self.surname} {self.name} {self.patronymic}, " \
            f"Дата рождения: {self.born}, ID читательского зала: {self.hall})"
