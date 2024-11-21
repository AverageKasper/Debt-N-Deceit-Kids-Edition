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
            money INT DEFAULT 0,
            carbon INT DEFAULT 0,
            inventory INT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()

def create_player(player_name, money=0.00, carbon=0, inventory=0):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO player (player_name, money, carbon, inventory) VALUES (%s, %s, %s, %s)
        """, (player_name, money, carbon, inventory))
        conn.commit()
initial_setup()
create_player('Kasper', 10000, 5000)