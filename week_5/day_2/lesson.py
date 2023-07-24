import psycopg2

# Conncetion to a database

connection = psycopg2.connect(
    database="Hollywood",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)

cursor = connection.cursor()

query = 'SELECT * FROM actor'

cursor.execute(query)

result = cursor.fetchall()

print(result)

cursor.close()
connection.close()

def get_all_actors():
  query = ''