# Welcome To My Version of Who's That Pokemon - Django Version
This is a standalone game taken from the Pokemon animated series "Who's That Pokemon" that was popular during our youth days.

NOTE: This guessing game will only have Pokemon from generation 1 - 3. Any Pokemon after that would not be here.

## How to play (WIP not near completion at all)
Very simple actually, there will be a random silhouette picture of a pokemon and the player's goal is to guess the name of the Pokemon. 

Each correctly guessed Pokemon would reward player a point on the score board. Any incorrect guess would simply skip the current image pokemon. (Not yet implemented)

## Work Priority 
* Focusing on deploying the game without silhouette.

## Future Work
* Add other generations to the game. Currently the system only have 1st generation Pokemon.
* Add silhouette onto Pokemon.
* Add scoreboard/ Highscores/ etc

### Prerequisites
```
Programming Language: Python 3+ (Rest In Peace Python 2)
Framework Required: Django Version 3+  
```

### Installing
I recommend installing and running code in a Python Virtual Environment which instills different version of Pythons. 

```
If using Git: 
  git clone https://github.com/KevinLu19/Pokemon.git
```
Or download repository code.

## Running the tests
In order to run on localhost, type onto terminal: 

```
python manage.py runserver
```

Will supply you with a local host URL (ex: localhost:8000 or 127.0. 0.1:8000)

## Purpose
The main reason for this project is to put the knowledge of Django into use by making a Pokemon guessing game. This is a remake of the Flask version of the exact same game. 

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - Main framwork used.
* [National PokeDex](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number) - Seek out the National PokeDex.

Languages: 
* Python 3
* HTML/ CSS / Jinja 
