from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

pg_db = PostgresqlExtDatabase("galaxy", port=5432, user='postgres', password="Saints504!", isolation_level=ISOLATION_LEVEL_SERIALIZABLE)

class BaseTable(Model):
    class Meta:
        database = pg_db

class Planet(BaseTable):
    name = CharField(null=False, index=True)

class Settlement(BaseTable):
    pass

class Item(BaseTable):
    pass

class Faction(BaseTable):
    pass

class Event(BaseTable):
    pass

class Actor(BaseTable):
    name = CharField(null=False, index=True)
    race = CharField(null=False, index=True)
    age = IntegerField(null=False, index=True)
    # profession = CharField(null=False, index=True)
    # forceSensitivity = BooleanField(null=False, index=True)
    # forceSkill = IntegerField(null=False, index=True)
    # meleeSkill = IntegerField(null=False, index=True)
    # rangedSkill = IntegerField(null=False, index=True)
    # agilitySkill = IntegerField(null=False, Index=True)
    # pilotingSkill = IntegerField(null=False, index=True)
    # stealthSkill = IntegerField(null=False, index=True)
    # tradeSkill = IntegerField(null=False, index=True)
    # # smugglingSkill = IntegerField(null=False, index=True)
    # leadershipSkiil = IntegerField(null=False, index=True)
    # strategySkill = IntegerField(null=False, index=True)
    # medicalSkill = IntegerField(null=False, index=True)
    # trackingSkill = IntegerField(null=False, index=True)
    # survivalSkill = IntegerField(null=False, index=True)
    # trappingSkill = IntegerField(null=False, index=True)
    # # engineeringSkill = IntegerField(null=False, index=True)
    # craftingSkill = IntegerField(null=False, index=True)
    # slicingSkill = IntegerField(null=False, index=True)
    # traits = ArrayField(null=False, index=True)
    # languages = ArrayField(null=False, index=True)
    # companions = ArrayField(null=False, index=True)
    
class User(Actor):
    pass

class playerInventory(Item):
    pass

