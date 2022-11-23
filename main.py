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
from Database.updateData import *
import psycopg2

def progressTime():
    # enter date into database for a default starting date

    # update date and update database everytime
    pass 

def devTest():
    testMenu = input("""
        1. Advance Time
        2. Add Inventory
        3. Remove Inventory
        4. View Inventory
        5. Back to Main Menu
        
        Choose an option: """)

    if testMenu == "1":
        advanceTime()
    elif testMenu == "2":
        randItems()
    elif testMenu == "3":
        pass
    elif testMenu == "4":
        getInventory()
    elif testMenu == "5":
        pass
    else:
        pass

def relationMenu():
    menu = input("""
        1. View Family
        2. Friends/Rivals
        3. All
        4. Search
        5. Back to Main Menu
        
        Choose an option: """)

    if menu == "1":
        print("")
        viewFamily(Actor.get().familyName)
    elif menu == "2":
        pass
    elif menu == "3":
        pass
    elif menu == "4":
        pass
    elif menu == "5":
        pass
    else:
        relationMenu()

def actionMenu():
    menu = input("""
        1. Skill Training
        2. Back To Main Menu
        
        Choose an option: """)
    
    if menu == "1":
        pass
    elif menu == "2":
        pass
    else:
        actionMenu()

def planetMenu():
    menu = input("""
        1. Starport
        2. Back To Main Menu
        
        Choose an option: """)
    
    if menu == "1":
        pass
    elif menu == "2":
        pass
    else:
        planetMenu()
    

def playerCard():
    # add the rest of the skills
    userDetails = User.get()

    playerName = userDetails.name
    playerFamily = userDetails.familyName
    playerRace = userDetails.race
    playerHomePlanet = userDetails.homePlanet
    # more player info - companions?
    cardString = f"""
        Name: {playerName} {playerFamily}
        Race: {playerRace}
        Home Planet: {playerHomePlanet}"""
    print(cardString)

    # add an inventory
    # add equiupment - ability to equip items
    # check skill numbers
    charMenu = input("""
        1. Inventory
        2. Equipment
        3. Skills
        4. Back to Main Menu
        
        Choose an option: """)

    if charMenu == "1":
        getInventory()
        playerCard()
    elif charMenu == "2":
        pass
    elif charMenu == "3":
        pass
    elif charMenu == "4":
        pass
    else:
        playerCard()

def createUser():
    # random gen names
    name = input("Enter your name: ")

    familyName = input("Enter Your Family Name: ")

    # add more races - race stat bonuses
    race = input("""
        1.Human     2.Human
        2.Human     3.Human
        3.Human     4.Human
        
        Choose a race: """)

    # make genuine list of planets - planet bonuses
    homePlanet = input("""
        1.Tatooine      2.Jakku
        3.Geonosis      4.Pasana
        5.Savareen      6.Jedha
        
        Choose a planet: """)

    if name.strip() == "" or race.strip == "" or homePlanet.strip() == "":
        print("dumbass")
        createUser()
    else:
        newUser(name, familyName, race, homePlanet)

def newGameMenu():
    print("Are You Sure?")

    choice = input("""
        Confirm (Y)es or (N)o: """)
    
    if choice == "Y" or choice == "y":
        newGame()
        createUser()
    elif choice == "N" or choice == 'n':
        return
    else:
        print("dumbass")
        newGameMenu()

def main():
    print("")
    print("S.W.G")
    print("")
    try:
        getDate()
    except:
        pass

    # Current situation Info on main screen

    # Settlement menu - locations
    #  Action menu?
    choice = input("""
        1. My Character
        2. Relationships
        3. Actions
        4. Planet
        D: Dev Test
        N. New Game?
        Q: Exit Game

        Please enter your choice: """)

    if choice == "1":
        playerCard()
        main()
    elif choice == "2":
        relationMenu()
        main()
    elif choice == "3":
        pass
    elif choice == "D" or choice == "d":
        devTest()
        main()
    elif choice == "N" or choice == "n":
        newGameMenu()
        main()
    elif choice == "q" or choice == "Q":
        pass
    else:
        print("dumbass")
        main()

def databaseExist():
    connection = None
    try:
        connection = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
    except:
        print('Database not connected.')

    if connection is not None:
        connection.autocommit = True

        cur = connection.cursor()

        cur.execute("SELECT datname FROM pg_database;")

        list_database = cur.fetchall()

        if ("galaxy",) in list_database:
            print("Galaxy Loaded")
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