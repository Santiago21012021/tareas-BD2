import sqlite3
conn = sqlite3.connect("adultos.db")
cursor = conn.cursor()

_SQL="""
create table if not exists Adultos(
cedula TEXT,
primernombre TEXT,
segundonombre TEXT,
primerapellido TEXT,
segundoapellido TEXT);
"""

with open("sql.sql", "r", encoding="UTF-8") as f:
    for i in f.read().split("\n"):
        cursor.execute(i)
        conn.commit()
        
        

