# Sql part for moneys and what else needs to be changed in the database
# Currencies in database: Money, CP
# Other stuff: Achievements, player logging, Items
from utilities import conn

def initial_setup():

    cursor = conn.cursor()
    sql = """IF OBJECT_ID('goal', 'U') IS NOT NULL DROP TABLE goal;
             IF OBJECT_ID('goal_reached', 'U') IS NOT NULL DROP TABLE goal_reached;
             ALTER TABLE game DROP COLUMN co2_consumed, co2_budget;"""
    cursor.execute(sql)

initial_setup()
