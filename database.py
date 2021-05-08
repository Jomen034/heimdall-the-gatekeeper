import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='heimdall',
    user='postgres',
    password='pgadmin'
)

cur = con.cursor()

cur.execute('insert into public."Test" (id, name, adress) values (%s, %s, %s)', (2, 'pardede', 'medan'))

cur.execute('select * from public."Test"')