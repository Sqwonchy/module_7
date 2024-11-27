import sqlite3

name_table = 'Products'

def initiate_db():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {name_table}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                price INT NOT NULL
            )
        ''')
        connection.commit()

def get_all_products():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'''
            SELECT * FROM {name_table}
        ''')
        return cursor.fetchall()

def add_product(products=list) -> None:
    """
    Добавить продукт в таблицу - name_table
    :param products: [list, list....]
    list = [ title= text, description= text, price= int]
    :return: None
    """
    try:
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            for product in products:
                cursor.execute(f"INSERT INTO {name_table} (title, description, price) VALUES (?, ?, ?)",
                               (product[0], product[1], product[2]))
            connection.commit()
    except Exception as e:
        print(f"Error occurred: {e}")


initiate_db()

if __name__ == "__main__":
    prod = [[f'Продукт {i+1}', f'Описание {i+1}', (i+1)*100] for i in range(4)]
    # add_product(prod)
