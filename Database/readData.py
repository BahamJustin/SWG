import os
from schema import *
from os import *
import random
import names
import psycopg2

planetTemplate = "{planet.name}"

def viewAllPlanets():
    print("All Planets")
    print("-" * 35)

    for planet in Planet.select():
        print(planetTemplate.format(planet=planet))

    pg_db.close()
        
viewAllPlanets()