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
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.recycleview import RecycleView

Window.size = (414, 736)

class WindowManager(ScreenManager):
    pass

wm = WindowManager()

class PlayerInfo:
    try:
            user = User.get()
    except:
            pass

    if user.forceSensitivity == 1:
        playerForceSense = "Yes"
    else:
        playerForceSense = "No"

class EquipmentScreen(Screen):
    pass

# grid with no bottom - scroll - different pages for each item type

class InventoryStack(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in PlayerInventory.select():
            size = dp(100)
            dictItem = model_to_dict(i) 
            invButton = Button(text=dictItem['name'], size_hint=(None, None), size=(size, size))
            self.add_widget(invButton)

    def add(self):
        pass
        
class InventoryScreen(Screen):
    pass        

class SkillScreen(Screen):
    skillInfo = f"""
        Force Sensitivty: {PlayerInfo.playerForceSense}
        Force Skill: {PlayerInfo.user.forceSkill}
        Melee: {PlayerInfo.user.meleeSkill}
        Ranged: {PlayerInfo.user.rangedSkill}
        Agility: {PlayerInfo.user.agilitySkill}
        Piloting: {PlayerInfo.user.pilotingSkill}
        Stealth: {PlayerInfo.user.stealthSkill}
        Trade: {PlayerInfo.user.tradeSkill}
        Smuggling: {PlayerInfo.user.smugglingSkill}
        Leadership: {PlayerInfo.user.leadershipSkill}
        Strategy: {PlayerInfo.user.strategySkill}
        Medical: {PlayerInfo.user.medicalSkill}
        Tracking: {PlayerInfo.user.trackingSkill}
        Slicing: {PlayerInfo.user.slicingSkill}
        Engineering: {PlayerInfo.user.engineeringSkill}"""

class CharacterMenu(Screen):
    playerInfo = f"""
    Name: {PlayerInfo.user.name} {PlayerInfo.user.familyName} 
    Age: {PlayerInfo.user.age}                     
    Race: {PlayerInfo.user.race}
    Home Planet: {PlayerInfo.user.homePlanet}"""

class RelationshipMenu(Screen):
    pass

class ActionMenu(Screen):
    pass

class PlanetMenu(Screen):
    pass
        
class DevTestMenu(Screen):
    def devAdvanceTime(self):
        advanceTime()
    
    def addInventory(self):
        randItems()

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

# Main Menu - Stack layout
class MainMenu(Screen):
    try:
        gameDate = StringProperty(getDate())
        userName = StringProperty(User.get().name)
    except:
        gameDate = StringProperty("No DB")
        userName = StringProperty("No DB")

    def getMainInfo(self, *largs):
        try:
            self.gameDate = getDate()
            self.userName = User.get().name
        except:
            pass
        # pg_db.close()

# Progress bar on botttom, lore skyrim style on top of progress bar, load icon in middle, when done, pull up main window
class TitleWindow(Screen):
    try:
        userName = StringProperty(PlayerInfo.user.name)
        userExists = True
    except:
        userName = "No Game"
        userExists = False

    def getTitleInfo(self, *largs):
        try:
            self.userName = User.get().name
            self.userExists = True
        except:
            pass

    def killDB(self):
        killDatabase()

class SWGApp(App):
    pass

if __name__ == "__main__":
    SWGApp().run()