# Sql part for moneys and what else needs to be changed in the database
# Currencies in database: Money, CP
# Other stuff: Achievements, player logging, Items
from utilities import conn

def initial_setup():
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS player (
            id SERIAL PRIMARY KEY,
            player_name VARCHAR(100) NOT NULL,
            location_id VARCHAR(100) DEFAULT 'EFHK',
            money INT DEFAULT 0,
            carbon INT DEFAULT 0,
            shark INT DEFAULT 0,
            inventory INT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()

def create_player(player_name, money, carbon, shark):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO player (player_name, money, carbon, shark) VALUES (%s, %s, %s, %s)
        """, (player_name, money, carbon, shark))
        conn.commit()

def get_money(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT money FROM player WHERE player_name = %s
        """, (player_name,))
        money = cursor.fetchall()
        return money[0][0]

def update_money(player_name, money):
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE player SET money = %s WHERE player_name = %s
        """, (money, player_name))
        conn.commit()

def get_carbon(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT carbon FROM player WHERE player_name = %s
        """, (player_name,))
        carbon = cursor.fetchall()
        return carbon[0][0]

def update_carbon(player_name, carbon):
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE player SET carbon = %s WHERE player_name = %s
        """, (carbon, player_name))
        conn.commit()

def fly(airport_type):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT name, iso_country, type FROM airport where contintent = 'EU' and type = '%s' ORDER BY RAND() LIMIT 1
        """, (airport_type,))
        location = cursor.fetchall()
        return location[0][0]
initial_setup()