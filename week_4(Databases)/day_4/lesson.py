import psycopg2

# Conncetion to a database

connection = psycopg2.connect(
    database="Hollywood",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)

# Placing cursor and collect data
def retrieve_actors():
  with connection:
    with connection.cursor() as curs:
      query = "select * from actor"
      curs.execute(query)
      data = curs.fetchall()
      print(data)

# executing function
retrieve_actors()

# ALTERNATE SOLUTION

# cursor = connection.cursor()

# # Making query

# query = 'SELECT * FROM actor'

# cursor.execute(query)

# result = cursor.fetchall()

# print(result)

# cursor.close()
# connection.close()

# def get_all_actors():
#   query = ''