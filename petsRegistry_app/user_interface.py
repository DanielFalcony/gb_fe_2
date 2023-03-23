import random
from animals import Animal
from animals_list import animal_type, animal_species, animal_name

all_animals = []


def show_all():
    for animal in all_animals:
        print(animal)


def add_new_animal():
    name = random.choice(animal_name)
    a_spec = random.choice(animal_species)
    if a_spec in ("Лошадь", "Верблюд", "Осел"):
        a_type = animal_type[1]
    else:
        a_type = animal_type[0]
    new_animal = Animal(name, a_spec, a_type)
    all_animals.append(new_animal)
    return new_animal


def add_command(anim_id, key, val):
    anim_true = all_animals.pop(anim_id - 1)
    anim_true.set_commands(key, val)
    all_animals.insert(anim_id - 1, anim_true)
