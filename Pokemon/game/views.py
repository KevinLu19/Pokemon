from django.shortcuts import render


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
    }
]


def home(request):
    
    context = {
        "posts" : posts
    }
        
    # Load Template that we included from settings.py
    return (render(request, "game/game.html", context))

def about(request):
    return (render(request, "game/about.html", {'title': 'about'}))
