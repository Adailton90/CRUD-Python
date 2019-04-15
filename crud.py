import mysql.connector
from mysql.connector.cursor import MySQLCursor

con = mysql.connector.connect(user='root', password='', host='localhost', database='escola_curso')

c = MySQLCursor(con)

def select(fields, tables, where=None):
    global c
    query = "select " + fields + " from " + tables
    if(where):
        query = query + " where " + where
    c.execute(query)
    return c.fetchall()

def insert(values, table, fields=None):
    global c, con
    query = "insert into " + table
    if(fields):
        query = query + " (" + fields + ") "
    query = query + " values " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit()

#criando uma variavel para poder usar no INSERT
values = [
    "default, 'Jonata Reis','2000-01-14', 'av das pedras, 123', 'Salvador', 'Ba', '12341567278'",
    "default, 'Maria joana','1990-02-14', 'av das ACM, 10', 'Salvador', 'Ba', '12341567212'"
    ]
def update(sets, table, where=None):
    global c, con
    query = "update " + table
    query = query + " set " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if(where):
        query = query + " where " + where

    c.execute(query)
    con.commit()

def delete(table, where):
    global c, con
    query = "delete from " + table + " where " + where

    c.execute(query)
    con.commit()

#inserindo registro
insert(values,"alunos")

#selecionando todos itens da tabela alunos
print(select("*", "alunos"))

#deletando um registro da tabela e mostrando que foi deletado
print(delete("alunos","id_alunos=9"))
print(select("*", "alunos", "id_alunos=9"))



