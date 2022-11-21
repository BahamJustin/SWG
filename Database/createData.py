import os
from Database.schema import *
from os import *
import random
import names
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def randNum():
    print(random.randrange(20, 65))

planets = (
    ("Tatooine"),
    ("Jakku"),
    ("Geonosis"),
    ("Pasaana"),
    ("Savareen"),
    ("Jedha")
)

race = (
    ("Human"),
    ("Twi'lek"),
    ("Togruta"),
    ("Cathar"),
)

items = (
    ("Gun"),
    ("Lightsaber"),
    ("Body Pillow"),
    ("iPhone With Flappy Bird"),
    ("gf"),
    ("PSP"),
    ("Golden Tabernacle")
)

factions = (
    ("Galactic Empire"),
    ("Rebel Alliance"),
    ("Hutt Cartel")
)

events = (
    ("a"),
    ("b"),
    ("c")
)

playerinventory = []

models = ([Planet, Settlement, Actor, Item, Faction, Event, User, playerInventory])

def newDatabase():
    conn = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
    cur = conn.cursor()

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute("DROP DATABASE IF EXISTS galaxy")
    cur.execute('CREATE DATABASE galaxy')

    conn.close()
    
def genGalaxy():
    pg_db.drop_tables(models)
    pg_db.create_tables(models)

    for planet in planets:
        Planet.create(name=planet)
        for settlement in range(1):
            if planet == "Tatooine":
                Settlement.create(
                    name="Mos Eisley",
                    homePlanet=planet
                )
                Settlement.create(
                    name="Mos Esfa",
                    homePlanet=planet
                )
            else:
                Settlement.create(
                    name="First",
                    homePlanet=planet
                )
                Settlement.create(
                    name="Second",
                    homePlanet=planet
                )
        for actor in range(5):
            Actor.create(
            name=names.get_first_name(),
            race=random.choice(race),
            homePlanet=planet
            )

    for item in items:
        Item.create(
            name=item
        )

    for faction in factions:
        Faction.create(
            name=faction
        )

    for event in events:
        Event.create(
            name=event
        )

        pg_db.close()

def newUser(name, race, homePlanet):
    pg_db.drop_tables(User)
    User.create(
        name=name,
        race=race,
        homePlanet=homePlanet
    )

def newGame():
    newDatabase()
    genGalaxy()