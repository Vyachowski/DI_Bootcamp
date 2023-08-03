# Exercise 1 : Restaurant Menu Manager
# Instructions
# Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.

# PART 1
# In this exercise we will use PostgreSQL and Python.

# 1) Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns
#    item_id : SERIAL PRIMARY KEY
#    item_name : VARCHAR(30) NOT NULL
#    item_price : SMALLINT DEFAULT 0
# 2) In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.
# 3) Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table. The update method can update the name as well as the price of an item.

# Codebox:

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all()

import psycopg2

def create_connection():
  return psycopg2.connect(
    database='test', user='root', password='icantrevealitsorry', host='localhost', port="5432"
  )

class MenuItem:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def save(self):
    query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)"
    values = (self.name, self.price)
    self._execute_query(query, values)

  def delete(self):
    query = "DELETE FROM Menu_Items WHERE item_name = %s"
    value = (self.name,)
    self._execute_query(query, value)

  def update(self, new_name, new_price):
    query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s"
    values = (new_name, new_price, self.name)
    self._execute_query(query, values)
    self.name = new_name
    self.price = new_price

  def __str__(self):
    return f"{self.name} - ${self.price}"

  @staticmethod
  def _execute_query(query, values=None):
    with create_connection() as connection:
      with connection.cursor() as cursor:
        cursor.execute(query, values)
        connection.commit()