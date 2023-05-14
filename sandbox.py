# # Iterating object
# object = {
#     'key': 'value',
#     'key2': 'value',
#     'key3': 'value'
# }

# for key in object:
#   print(type(key))

# for key in object.items():
#   print(key)

# float_list = [num * 0.5 for num in range(3, 11)]
# print(float_list)


list1 = ['hello', 'hope', 'hate', 'bit', 'basket', 'code', 'come', 'chess', 'hack']
d = {}

for word in list1:
    d.setdefault(word[0], []).append(word)
list2 = list(d.values())
print(d)
print(list2)