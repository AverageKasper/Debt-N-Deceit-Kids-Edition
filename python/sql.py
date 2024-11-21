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
            inventory INT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()

def create_player(player_name, money=0.00, carbon=0):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO player (player_name, money, carbon) VALUES (%s, %s, %s)
        """, (player_name, money, carbon))
        conn.commit()

def get_money(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT money FROM player WHERE player_name = %s
        """, (player_name,))
        money = cursor.fetchall()
        return money[0][0]

initial_setup()