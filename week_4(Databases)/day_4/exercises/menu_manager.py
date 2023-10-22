# 1) In the file menu_manager.py, create a new class called MenuManager
# 2) Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.
# 3) Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.

from menu_item import MenuItem, create_connection

class MenuManager:
  @classmethod
  def get_by_name(cls, name):
    query = "SELECT * FROM Menu_Items WHERE item_name = %s"
    value = (name,)
    result = cls._execute_query(query, value)

    if result:
      item = result[0]
      return MenuItem(item[1], item[2])
    else:
      return None

  @classmethod
  def all_items(cls):
    query = "SELECT * FROM Menu_Items"
    results = cls._execute_query(query)

    menu_items = []
    for item in results:
      menu_items.append(f"{item[1]} - ${item[2]}")

    return menu_items

  @staticmethod
  def _execute_query(query, values=None):
    with create_connection() as connection:
      with connection.cursor() as cursor:
        cursor.execute(query, values)
        return cursor.fetchall()
      
if __name__ == "__main__":
  item = MenuItem('Burger', 35)
  # item.save()
  # # item.delete()
  # item.update('Veggie Burger', 37)
  item2 = MenuManager.get_by_name('Burger')
  print(item2)
  items = MenuManager.all_items()
  print(items)