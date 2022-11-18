import os
from schema import *
from os import *
import random
import names
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
cur = conn.cursor()

planets = (
    ("Tatooine"),
    ("Jakku"),
    ("Geonosis"),
    ("Pasaana"),
    ("Savareen"),
    ("Jedha")
)

playerinventory = []

models = ([Planet])

def newDatabase():
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute("DROP DATABASE IF EXISTS galaxy")
    cur.execute('CREATE DATABASE galaxy')
    
    conn.close()
    
def newGalaxy():
    pg_db.drop_tables(models)
    pg_db.create_tables(models)

    for planet in planets:
        Planet.create(name=planet)
    
    pg_db.close()

def newGame():
    newDatabase()
    newGalaxy()

newGame()