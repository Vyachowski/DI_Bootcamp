from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families
import json


# Create your views here.
def display_all_animals(request):

    cleaned_animals = []

    for animal in animals:
        cleaned_animal = animal.copy()
        del cleaned_animal["id"]
        cleaned_animals.append(cleaned_animal)

    result = "\n\n".join(json.dumps(cleaned_animal, indent=4) for cleaned_animal in cleaned_animals)

    return HttpResponse(result, content_type="application/json")


def display_all_families(request):
    animals = list(map(lambda family: f"{family['name']}<br>", families))
    return HttpResponse(animals)

def display_one_animal(request, animal_id):
    # animal = animals[animal_id - 1]['name']
    # return HttpResponse(animal)
    if 1 <= animal_id <= len(animals):
        animal = animals[animal_id - 1]
        cleaned_animal = animal.copy()
        del cleaned_animal['id']

        result = json.dumps(cleaned_animal, indent=4)
        return HttpResponse(result, content_type='application/json')
    else:
        return HttpResponse('Animal not found')

def display_animal_per_family(request, family_id):
    animals_in_family = [animal for animal in animals if animal['family'] == family_id]
    return HttpResponse(animals_in_family)