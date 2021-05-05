from mysql.connector import connect

with connect(host="localhost", user="root", password="ga2468bi") as conn:
    print(conn)
