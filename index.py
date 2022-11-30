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

Window.size = (720, 1080)

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

class NewGameMenu(Screen):
    def startNewGame(self):
        newGame()

# Main Menu - Stack layout
class MainMenu(Screen):
    gameDate = StringProperty(getDate())
    def on_pre_enter(self, *largs):
        newDate = getDate()
        print(newDate)
        self.gameDate = newDate

# Progress bar on botttom, lore skyrim style on top of progress bar, load icon in middle, when done, pull up main window
class LoadWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class SWGApp(App):
    pass

SWGApp().run()