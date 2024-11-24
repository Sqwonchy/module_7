"""
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
COUNT
SUM
AVG
MAX
MIN
cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{n}", f"example{n}@gmail.com", f"{n*10}"))  метод для добавления  юзернейм почта и возраст баланс
cursor.execute("UPDATE Users SET age = ? WHERE username = ?", ("25", "newuser") )    метод для обновления возраста по юзернейму
cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",))  метод удаления по юзернайму
"""
# __________________________________________________________________________________________________________________
import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE  IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)

''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#     n = i+1
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{n}", f"example{n}@gmail.com", n*10, 1000))
#
#
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE  id%2 == 0 ")
# cursor.execute("UPDATE Users SET balance = 500 WHERE id%2")
# cursor.execute("DELETE FROM Users Where id % 3 == 1 ")
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE  age != 60 ")
#
# res = cursor.fetchall()
# for i in res:
#     print(f"Имя:{i[0]}| Почта: {i[1]}| Возраст: {i[2]}|Баланс:{i[3]}")

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
res_1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
res_2 = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users")
res_3 = cursor.fetchone()[0]
res_3_1 = res_2/res_1  
print(res_1)
print(res_2)
print(res_3)
print(res_3_1)

connection.commit()
connection.close()