# NOT READY YET, YESTERDAY HAD AN ADDITIONAL CLASS IN COLLEGE SO I AM FINISHING IT AT THE MORNING

# Instructions
# Using this REST Countries API, create the functionality which will write 10 random countries to your database.
# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.
    
import requests, random, sqlite3

def get_random_countries(amount):
  response = requests.get('https://restcountries.com/v3.1/all')
  countries = response.json()
  random_countries = random.sample(countries, amount)
  return random_countries