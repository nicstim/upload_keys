import psycopg2
import random
import datetime
# from datetime import timezone

import time
d = datetime.date(2020,7,2)
con = psycopg2.connect(
  database="educa",
  user="admin",
  password="admin",
  host="127.0.0.1",
  port="5432"
)
print(type(d))
print(d)
varieble = [1,2,3,4,5]
cur = con.cursor()
users = []
cur.execute("SELECT fio from account_LearningList")
rows = cur.fetchall()
for row in rows:
    row = str(row)
    for char in row:
        if char == ',' or char == '(' or char == ')' or char == "'":
            row = row.replace(char,'')
        else:
            pass
    users.append(row)
# print(users)
d_name = [
    "Численные методы",
    "Инженерная графика",
    "Теория информации и кодировани",
    "Правоведение",
    "Дискретная математика",
    "Методы программирования",
    "Философия",
    "Физика",
    "Операционные системы",
    "Схемотехника"
    ]
i = 1
for user in users:
    for dis in d_name:
        var = varieble[random.randint(0,len(varieble)-1)]
        cur.execute(f"INSERT INTO account_gradebook(id_stud,data,name_stud_id,mark_stud_id,name_discipline_id) VALUES({i},{time.time()},'{user}',{var},'{dis}')")
        i+=1
        con.commit()
