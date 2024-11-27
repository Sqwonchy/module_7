import sqlite3

name_table = 'Users'
file_db = 'not_telegram.db'

def initiate_db():
    with sqlite3.connect(file_db) as connection:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE  IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
                )
        ''')
        connection.commit()

def is_included(username):
    with sqlite3.connect(file_db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE LOWER(username) = LOWER(?)", (username,))
        result = cursor.fetchone()
        return result is not None

def add_user(username, email, age):
    try:
        with sqlite3.connect(file_db) as connection:
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO {name_table} (username, email, age, balance) VALUES (?, ?, ?, ?)",
                         (username, email, age, 1000))
            connection.commit()
    except Exception as e:
        print(f"Произошла ошибка: {e}")




initiate_db()


if __name__ == "__main__":
    pass