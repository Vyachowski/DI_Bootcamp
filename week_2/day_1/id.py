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

# In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years

my_age = 34
next_stop = my_age + 123879
print(next_stop)

first_name = 'Slava'
last_name = 'Haikin'
print(first_name + ' ' + last_name)

name = 'John Doe'
if len(name) > 20:
    print(f'Name "{name}" is more than 20 chars long')
    length_description = 'long'
elif len(name) > 20:
    print(f'Name "{name}" is more than 15 chars long')
    length_description = 'semi long'
elif len(name) > 20:
    print(f'Name "{name}" is more than 10 chars long')
    length_description = 'semi long'
elif len(name) > 20:
    print(f'Name "{name}" is 8, 9 or 10 chars long')
    length_description = 'semi short'
else:
    print(f'Name "{name}" is a short name')
    length_description = 'short'