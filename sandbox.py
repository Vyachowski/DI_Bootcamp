# Iterating object
object = {
    'key': 'value',
    'key2': 'value',
    'key3': 'value'
}

for key in object:
  print(type(key))

for key in object.items():
  print(key)