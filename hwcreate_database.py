from faker import Faker

from hw_db_160624.databasehw import create_dbhw, Session
from hw_db_160624.readers import Readers
from hw_db_160624.entertainment_hall import Entertainment_hall
from hw_db_160624.books import Books

def create_database(load_fake_data=True):
    create_dbhw()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session):
    name_books = ['Творчество Шекспира', 'Сила воли', 'Подсознание может все',
                  'Счастливое детство', 'Как стать великим', 'Успех', 'Как научить мозг учиться',
                  'Как искуccтво влияет на мозг', 'Мозг и творчество', 'Мозг и его различия по половому признаку',
                  'Откуда берутся мысли', 'Почему наш мир таков, каков он есть', 'Чеширская улыбка кота Шрёдингера']

    hall1 = Entertainment_hall(hall="Red_hall")
    hall2 = Entertainment_hall(hall="Green_hall")
    session.add(hall1)
    session.add(hall2)

    for key, it in enumerate(name_books):
        book = Books(name_b=it)
        book.entertainment_hall.append(hall1)
        if key % 2 == 0:
            book.entertainment_hall.append(hall2)
        session.add(book)

    session.commit()

    faker = Faker("ru_RU")
    hall_list = [hall1, hall2]

    for _ in range(50):
        full_name = faker.name().split()
        born = faker.random.randint(14, 79)
        hall = faker.random.choice(hall_list)
        reader = Readers(full_name, born, hall.id)
        session.add(reader)

    session.commit()
    session.close()



