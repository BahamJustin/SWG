from peewee import *
from pathlib import Path
import csv
import sys
import os
import random
from consolemenu import *
from consolemenu import SelectionMenu
from consolemenu.items import *
from Database.createData import *
from Database.readData import *
import psycopg2

def createUser():
    name = input("Type your name: ")

    race = input("""
        1.Human     2.Human
        2.Human     3.Human
        3.Human     4.Human
        
        Choose a race: """)

    homePlanet = input("""
        1.Tatooine      2.Jakku
        3.Geonosis      4.Pasana
        5.Savareen      6.Jedha
        
        Choose a planet: """)

    if name.strip() == "" or race.strip == "" or homePlanet.strip() == "":
        print("dumbass")
        createUser()
    else:
        newUser(name, race, homePlanet)

    # if 'name' in locals():
    #     print(name + " Exists")
    # elif 'name' == "Justin":
    #     print("dumbass")
    # elif name == "":
    #     print("empty")

def newGameMenu():
    print("Are You Sure?")

    choice = input("""
                        Confirm (Y)es or (N)o
                        
                        """)
    
    if choice == "Y" or choice == "y":
        newGame()
        createUser()
    elif choice == "N" or choice == 'n':
        return

def main():
    print("")
    print("SWG")
    print("")

    if User.name in locals():
        print("Name Here")

    choice = input("""
        1. Show Name
        N. New Game?
        Q: Exit Game

        Please enter your choice: """)

    if choice == "1":
        main()
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "N" or choice == "n":
        newGameMenu()
        main()
    elif choice == "q" or choice == "Q":
        pass
    else:
        pass

def databaseExist():
    connection = None
    try:
        # In PostgreSQL, default username is 'postgres' and password is 'postgres'.
        # And also there is a default database exist named as 'postgres'.
        # Default host is 'localhost' or '127.0.0.1'
        # And default port is '54322'.
        connection = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')

    except:
        print('Database not connected.')

    if connection is not None:
        connection.autocommit = True

        cur = connection.cursor()

        cur.execute("SELECT datname FROM pg_database;")

        list_database = cur.fetchall()

        if ("galaxy",) in list_database:
            main()
        else:
            print("Starting a new game")
            newGame()
            createUser()
            main()
        connection.close()

def startGame():
    print("Checking for Galaxy")
    databaseExist()

startGame()