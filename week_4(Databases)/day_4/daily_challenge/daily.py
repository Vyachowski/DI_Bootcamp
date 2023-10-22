# Instructions
# 1) Using this REST Countries API, create the functionality which will write 10 random countries to your database.
# 2) These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.
    
import requests, random, sqlite3, os

dirname = os.getcwd()
database_path = f'{dirname}/week_4/day_4/daily_challenge/countries.db'

def get_random_countries(amount = 10):
  response = requests.get('https://restcountries.com/v3.1/all')
  countries = response.json()
  random_countries = random.sample(countries, amount)
  return random_countries

with sqlite3.connect(database_path) as connect:
    cursor = connect.cursor()

create_table = '''
        CREATE TABLE IF NOT EXISTS countries (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          capital TEXT,
          flag TEXT,
          subregion TEXT,
          population INTEGER CHECK (population >= 0)
        );
        '''

cursor.execute(create_table)
random_countries = get_random_countries()

for country in random_countries:
    name = country.get('name', {}).get('common')
    capital = country.get('capital', ['N/A'])[0]
    flag = country.get('flag', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)

    insert_query = '''
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (?, ?, ?, ?, ?)
        '''
    cursor.execute(insert_query, (name, capital, flag, subregion, population))

connect.commit()
connect.close()

# OUTPUT TEST

connect = sqlite3.connect(database_path)
cursor = connect.cursor()

select_query = '''
    SELECT * FROM countries
'''

cursor.execute(select_query)
all_rows = cursor.fetchall()

for row in all_rows:
    print(row)

connect.close()