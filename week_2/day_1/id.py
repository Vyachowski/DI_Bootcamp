username = 'Tom'
my_name = username

# Checking id
username_id = id(username)
my_name_id = id(my_name)


print('username', username)
print('my_name', my_name)

username = 'Emma'
print('username', username)
print('my_name', my_name)

# Checking id again
username_id = id(username)
my_name_id = id(my_name)

# STRINGS ARE IMMUTABLE IN PYTHON

print(username_id)
print(my_name_id)