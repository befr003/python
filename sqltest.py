import sqlite3
connection = sqlite3.connect('client.db',check_same_thread=False)
cursor = connection.cursor()
def start():
    create_table = "create table if not exists client (id integer PRIMARY KEY AUTOINCREMENT, name text, country text ) "
    cursor.execute(create_table)
    connection.commit
    init_data()

def init_data():
    clients = [(1, "bob", "SE"), (2, "fof", "SE")]
    insert_query = "REPLACE INTO client VALUES (?,?,?)"
    cursor.executemany(insert_query, clients)
    connection.commit()

def read_all():
    select_sql = "SELECT * FROM client"
    result = cursor.execute(select_sql)
    return result.fetchall()

def read(id):
    select_sql = "SELECT * FROM client where id = (?)"
    result = cursor.execute(select_sql, (id,))
    return result.fetchone()    

def add_data(name, country):
    client = (name, country)
    insert_query = "insert INTO client VALUES (null, ?,?)"
    cursor.execute(insert_query, client)
    connection.commit()

def update_data(id, name, country):
    client = (id, name, country)
    insert_query = "REPLACE INTO client VALUES (?,?,?)"
    cursor.execute(insert_query, client)
    connection.commit()

def close():
    connection.close()

start()

print(read(2))
print("done")

