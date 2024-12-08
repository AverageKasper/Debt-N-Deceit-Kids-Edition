# Sql part for moneys and what else needs to be changed in the database
# Currencies in database: Money, CP
# Other stuff: Achievements, player logging, Items
import mysql.connector
from flask import Blueprint, jsonify, Response

sql_blueprint = Blueprint('sql', __name__)

conn = mysql.connector.connect(
                host='localhost',
                database='flight_game',
                user='group_international',
                password='EEKPAMSMAW',
                autocommit=True,
                collation="utf8mb4_general_ci"
                )

def initial_setup():
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS player (
            id SERIAL PRIMARY KEY,
            player_name VARCHAR(100) NOT NULL,
            location_id VARCHAR(100) DEFAULT 'Finland',
            money INT DEFAULT 0,
            carbon INT DEFAULT 0,
            shark INT DEFAULT 0,
            inventory INT DEFAULT 0
            );
        """)
        conn.commit()

def create_player(player_name, money, carbon, shark):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO player (player_name, money, carbon, shark) VALUES (%s, %s, %s, %s)
        """, (player_name, money, carbon, shark))
        conn.commit()

@sql_blueprint.route('/check_name/<player_name>')
def check_name(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT player_name FROM player WHERE player_name = %s
        """, (player_name,))
        name = cursor.fetchall()
        if cursor.rowcount > 0:
            return jsonify({"exists": True})
        else:
            return jsonify({"exists": False})

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

def get_shark(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT shark FROM player WHERE player_name = %s
        """, (player_name,))
        shark = cursor.fetchall()
        return shark[0][0]
    
def update_shark(player_name, shark):
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE player SET shark = %s WHERE player_name = %s
        """, (shark, player_name))
        conn.commit()

def get_inventory(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT inventory FROM player WHERE player_name = %s
        """, (player_name,))
        inventory = cursor.fetchall()
        return inventory[0][0]

def update_inventory(player_name, inventory):
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE player SET inventory = %s WHERE player_name = %s
        """, (inventory, player_name))
        conn.commit()

@sql_blueprint.route('player_stats/<player_name>')
def player_stats(player_name):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT money, carbon, shark, inventory FROM player WHERE player_name = %s
                       """, (player_name,))
        stats = cursor.fetchall()
        if stats:
            stats_json = {
                "money": stats[0][0],
                "carbon": stats[0][1],
                "shark": stats[0][2],
                "inventory": stats[0][3]
            }
            return jsonify(stats_json)
        else:
            return jsonify({"error": "Player not found"}), 404

@sql_blueprint.route('/fly/<airport_type>')
def fly(airport_type):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT name, iso_country, type, ident, latitude_deg, longitude_deg FROM airport where continent = 'EU' and type = %s and name not like '%?%' ORDER BY RAND() LIMIT 1;
        """, (airport_type,))
        location = cursor.fetchone()
        if location:
            location_data = {
                "name": location[0],
                "iso_country": location[1],
                "type": location[2],
                "ident": location[3],
                "latitude_deg": location[4],
                "longitude_deg": location[5]
            }
            return jsonify(location_data)
        else:
            return jsonify({"error": "No airport found"}), 404

def update_location(player_name, icao):
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE player SET location_id = %s WHERE player_name = %s
        """, (icao, player_name))
        conn.commit()

initial_setup()


