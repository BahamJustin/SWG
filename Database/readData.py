import os
from os import *
import random
import names
import psycopg2
from consolemenu import *
from consolemenu.items import *
from Database.schema import *

planetTemplate = "{planet.name}"
actorTemplate = "{actor.name} {actor.familyName} {actor.race} {actor.homePlanet}"
settleTemplate = "{settlement.name} {settlement.homePlanet}"
itemTemplate = "{item.name}"

def viewAllPlanets():
    print("All Planets")
    print("-" * 35)

    for planet in Planet.select():
        print(planetTemplate.format(planet=planet))

    Screen().input('Press [Enter] to continue')

    pg_db.close()

def settlementsByPlanet(planet):
    print("Settlements of " + planet)
    print("-" * 35)

    for settlement in Settlement.select().where(Settlement.homePlanet == planet):
        print(settleTemplate.format(settlement=settlement))

    Screen().input('Press [Enter] to continue')

    pg_db.close()

def viewAllActors():
    print("All Actors")
    print("-" * 35)

    for actor in Actor.select():
        print(actorTemplate.format(actor=actor))

    Screen().input('Press [Enter] to continue')

    pg_db.close()

def actorsByPlanet(planet):   
    print("All Inhabitants of " + planet)
    print("-" * 35)

    for actor in Actor.select().where(Actor.homePlanet == planet):
        print(actorTemplate.format(actor=actor))

    Screen().input('Press [Enter] to continue')

    pg_db.close()
        
def viewAllItems():
    print("All Items")
    print("-" * 35)

    for item in Item.select():
        print(itemTemplate.format(item=item))

    Screen().input('Press [Enter] to continue')

    pg_db.close()

def viewFamily(familyName):
    print("Family Members")
    print("-" * 35)

    for actor in Actor.select().where(Actor.familyName == familyName):
        print(actorTemplate.format(actor=actor))

    Screen().input('Press [Enter] to continue')

    pg_db.close()