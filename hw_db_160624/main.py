import os
from hw_db_160624.databasehw import DATABASE_NAME
import hwcreate_database as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

