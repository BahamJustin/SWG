import os
from schema import *
from os import *
import random
import names
import psycopg2

planetTemplate = "{planet.name}"
actorTemplate = "{actor.name} {actor.race} {actor.homePlanet}"
settleTemplate = "{settlement.name} {settlement.homePlanet}"
itemTemplate = "{item.name}"

def viewAllPlanets():
    print("All Planets")
    print("-" * 35)

    for planet in Planet.select():
        print(planetTemplate.format(planet=planet))

    pg_db.close()

def settlementByPlanet(planet):
    print("Settlements of " + planet)
    print("-" * 35)

    for settlement in Settlement.select().where(Settlement.homePlanet == planet):
        print(settleTemplate.format(settlement=settlement))

    pg_db.close()

def viewAllActors():
    print("All Actors")
    print("-" * 35)

    for actor in Actor.select():
        print(actorTemplate.format(actor=actor))

    pg_db.close()

def actorByPlanet(planet):
    print("All Inhabitants of " + planet)
    print("-" * 35)

    for actor in Actor.select().where(Actor.homePlanet == planet):
        print(actorTemplate.format(actor=actor))

    pg_db.close()
        
def viewAllItems():
    print("All Items")
    print("-" * 35)

    for item in Item.select():
        print(itemTemplate.format(item=item))

    pg_db.close()

viewAllItems()