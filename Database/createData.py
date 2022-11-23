import os
from Database.schema import *
# from schema import *
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

weapons = (
    ("Gun"),
    ("Lightsaber")
)

miscItems = (
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

models = ([Planet, Settlement, Actor, Item, Faction, Event, User, PlayerInventory, Date])

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
        for actor in range(5):\
            # create star wars name gen
            Actor.create(
            name=names.get_first_name(),
            familyName=names.get_last_name(),
            race=random.choice(race),
            homePlanet=planet
            )

    for item in miscItems:
        Item.create(
            name=item,
            itemType = "Misc"
        )

    for weapon in weapons:
        Item.create(
            name=weapon,
            itemType = "Weapon" 
        )

    for faction in factions:
        Faction.create(
            name=faction
        )

    for event in events:
        Event.create(
            name=event
        )

    Date.create(
        month=1,
        year=4
    )

    pg_db.close()

def randItems():
    # put randmisc into inventory, then view inventory
    for item in Item.select().where(Item.itemType == "Weapon").order_by(fn.Random()).limit(1):
        PlayerInventory.create(
            name=item.name,
            itemType=item.itemType
        )

    for item in Item.select().where(Item.itemType == "Misc").order_by(fn.Random()).limit(1):
        PlayerInventory.create(
            name=item.name,
            itemType=item.itemType
        )

def newUser(name, familyName, race, homePlanet):
    pg_db.drop_tables(User)
    pg_db.drop_tables(PlayerInventory)
    User.create(
        name=name,
        familyName=familyName,
        race=race,
        homePlanet=homePlanet
    )

    randItems()

    for actor in range(2):
        Actor.create(
            name=names.get_first_name(),
            familyName=familyName,
            race=race,
            homePlanet=homePlanet,
        )

def newGame():
    newDatabase()
    genGalaxy()

