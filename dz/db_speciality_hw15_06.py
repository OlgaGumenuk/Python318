import sqlite3

specialities_list = [
    ('The economics of the organization', 18900, 6),
    ('Human resource management', 18900, 5),
    ('Marketing', 18900, 8),
    ('Cybersecurity', 18900, 7),
    ('Management', 18900, 4),
    ('The global economy', 18900, 5),
    ('Logistics', 18900, 4),
    ('State administration', 18900, 4),
    ('Graphic design', 18900, 4),
    ('Jurisprudence', 18900, 4)
]

with sqlite3.connect("speciality.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS speciality(
        spec_ty_id INTEGER PRIMARY KEY AUTOINCREMENT,
        specialities TEXT,
        price INTEGER,
        period_of_study INTEGER
    )
    """)

    # for sp in specialities_list:
    #     cur.execute("INSERT INTO speciality VALUES(NULL, ?, ?, ?)", sp)

    cur.executescript("""
    DELETE FROM speciality WHERE period_of_study LIKE '8';
    UPDATE speciality SET period_of_study = period_of_study + 1;
    INSERT INTO speciality VALUES(NULL, 'Philosophy', 21000, 3;
    """)
