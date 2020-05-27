from django.shortcuts import render
from django.template.response import TemplateResponse

import random

posts = [
    {
        "author" : "Rumi",
        "title"  : "Post 1",
        "content": "First post",
        "date"   : "April 3, 2020"
    },
    {
        "author" : "Kevin",
        "title"  : "Post 2",
        "content": "Second post",
        "date"   : "April 5, 2020"
    },
]

def randomPokemonImage():
    image_number = int (493 * (1 - random.random()))

    return image_number

def home(request):
    # randomPokemonImage() is a callable function which will result in an error as it will return a value.
    # Therefore, calling function by its name only.
    pokemon_image_number = randomPokemonImage
    full_pokemon_file = str(pokemon_image_number) + ".png"

    context = {
        "posts" : posts,
        "image_file": full_pokemon_file,
    }

    # Load Template that we included from settings.py
    return (render(request, "game/game.html", context))


def about(request):
    return (render(request, "game/about.html", {'title': 'about'}))
