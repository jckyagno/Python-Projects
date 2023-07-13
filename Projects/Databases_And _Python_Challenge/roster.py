import sqlite3
from sqlite3 import Error


def create_connection():    # create a database connection to a
                            # database that resides in the memory
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists Roster( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            Name TEXT, \
            Species TEXT, \
            IQ TEXT \
            );")
        conn.commit()
        cur.execute("SELECT * FROM Roster")
        cur.execute("INSERT INTO Roster(Name, Species, IQ) \
            VALUES ('Jean-Baptiste Zorg', 'Human', '122'), \
            ('Korben Dallas', 'Meat Popsicle', '100'), \
            ('Ak''not', 'Mangalore', '-5') \
            ;")
        conn.commit()
        cur.execute("SELECT * FROM Roster")
        result = cur.fetchall()
        print("\n")
        for row in result:
            print(row)

        cur.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas';")
        conn.commit()
        cur.execute("SELECT * FROM Roster")
        result = cur.fetchall()
        print("\n")
        for row in result:
            print(row)

        cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human';")
        result = cur.fetchall()
        print("\n")
        for row in result:
            print(row)
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection()
