from main import *
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
from Database.emergencyKill import killDatabase
import psycopg2
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

Window.size = (414, 736)

class CharacterMenu(Screen):
    pass

class RelationshipMenu(Screen):
    pass

class ActionMenu(Screen):
    pass

class PlanetMenu(Screen):
    pass
        
class DevTestMenu(Screen):
    def devAdvanceTime(self):
        advanceTime()

class CreateUserMenu(Screen):
    userName = StringProperty("UserName")
    familyName = StringProperty("FamName")
    userRace = StringProperty("Race")
    userHome = StringProperty("Home Planet")

    def on_text_validate(self, widget):
        self.userName = widget.text
        newUser(self.userName, self.familyName, self.userRace, self.userHome)

class NewGameMenu(Screen):
    def startNewGame(self):
        newGame()

# Main Menu - Stack layout - variables dont update anymore??????
class MainMenu(Screen):
    gameDate = StringProperty(getDate())
    userName = User.get().name


    def getMainInfo(self, *largs):
        try:
            newDate = getDate()
            newName = User.get().name
            self.gameDate = newDate

            self.userName = newName
        except:
            pass
        # pg_db.close()

# Progress bar on botttom, lore skyrim style on top of progress bar, load icon in middle, when done, pull up main window
class LoadWindow(Screen):
    userExists = False

    try:
        userName = User.get().name
        userExists = True
    except:
        pass

    def getLoadInfo(self, *largs):
        try:
            userName = User.get().name
            userExists = True
        except:
            pass

    def killDB(self):
        killDatabase()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("SWG.kv")

class SWGApp(App):
    pass
    # connection = None
    # try:
    #     connection = psycopg2.connect(host='localhost', user='postgres', password='Saints504!')
    # except:
    #     print('Database not connected.')

    # if connection is not None:
    #     connection.autocommit = True

    #     cur = connection.cursor()

    #     cur.execute("SELECT datname FROM pg_database;")

    #     list_database = cur.fetchall()

    #     if ("galaxy") in list_database:
    #         print("Galaxy Loaded")
    #     else:
    #         print("Starting a new game")
    #     connection.close()

if __name__ == "__main__":
    SWGApp().run()