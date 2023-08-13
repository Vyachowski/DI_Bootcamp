from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
name = 'Bob Smith'
age = 35
country = 'USA'


def display_person(request):
    result = f'<h2>Name - {name}</h2><p>age - {age}</p><p>Country - {country}</p>'
    return HttpResponse(result)


people = ['bob','martha', 'fabio', 'john']


def display_people(request):
    sorted_people = sorted(people)
    result = '<h1>People of My Exercise</h1>'

    for person in sorted_people:
        person_capitalized = person.split(" ")[0].capitalize()
        result += '<h2>' + person_capitalized + '</h2>'

    return HttpResponse(result)


all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


def display_all_people(request):
    sorted_people = sorted(all_people, key=lambda persona: persona['age'])

    result = '<h1>People Sorted by Age</h1>'
    for person in sorted_people:
        result += f'<h2>Name: {person["name"]}</h2>'
        result += f'<p>Age: {person["age"]}</p>'
        result += f'<p>Country: {person["country"]}</p>'

    return HttpResponse(result)
