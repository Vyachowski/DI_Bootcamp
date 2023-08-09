from django.shortcuts import render
from django.http import HttpResponse
from info.data import animals, families

# Create your views here.
def display_all_animals(request):
    return HttpResponse(animals)

def display_all_families(request):
    animals = list(map(lambda family: family['name'] + ' ', families))
    return HttpResponse(animals)

def display_one_animal(request, animal_id):
    animal = animals[animal_id - 1]['name']
    return HttpResponse(animal)

def display_animal_per_family(request, family_id):
    animals_in_family = [animal for animal in animals if animal['family'] == family_id]
    return HttpResponse(animals_in_family)