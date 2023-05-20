# --- Modules --- #

# IMPORT

import requests
import time
import pprint 

# CODE

def get_pages_load_time(urls):
    try:
      if type(urls) != list and type(urls) != str:
        raise TypeError('Sorry, should be a list or a string')
      if type(urls) == list:
        for url in urls:
          if type(url) != str:
            raise TypeError('Sorry, every element of url\'s list should be a list')
    except TypeError as e:
      print(e)
    else:
      if type(urls) == str: 
        urls = urls.split()
      result = {}
      for url in urls:
        start_time = time.time()
        requests.get(url)
        end_time = time.time()
        load_time = end_time - start_time
        result[url] = str(round(load_time, 3)) + ' milliseconds'
      return pprint.pprint(result)

# OUTPUT

websites = ['https://www.google.com', 'https://www.ynet.co.il', 'https://www.imdb.com', 'https://www.ya.ru', 'https://www.codebless.me']
website = 'https://www.yahoo.com'
print(get_pages_load_time(websites))
print(get_pages_load_time(website))

# Part 1 : Quizz :
# Answer the following questions

# What is a class?
'''Class is a blueprint to create instances. It combines attributes a methods, both are encapsulated from other data'''
# What is an instance?
'''Instance is the implementation of the class'''
# What is encapsulation?
'''Encapsulation is a way to restrict direct acces to some infi inside the class'''
# What is abstraction?
'''It is a way to hide a big amount of data by one name to reduce complexity of the created system'''
# What is inheritance?
'''It is a property of classes to use a methods or attributes in children of the class'''
# What is multiple inheritance?
'''Multiple inheritance is when children inherit attributes or methods from two or more classes'''
# What is polymorphism?
''''''
# What is method resolution order or MRO?