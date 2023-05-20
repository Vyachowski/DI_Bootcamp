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