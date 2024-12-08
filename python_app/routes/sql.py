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
    cursor = None
    try:
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
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()

def create_player(player_name, money, carbon, shark):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO player (player_name, money, carbon, shark) VALUES (%s, %s, %s, %s)
            """, (player_name, money, carbon, shark))
            conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()

@sql_blueprint.route('/check_name/<player_name>')
def check_name(player_name):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT player_name FROM player WHERE player_name = %s
            """, (player_name,))
            name = cursor.fetchone()
            if name:
                return jsonify({"exists": True})
            else:
                return jsonify({"exists": False})
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()

def update_money(player_name, money):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE player SET money = %s WHERE player_name = %s
            """, (money, player_name))
            conn.commit()
            return  
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()

def update_carbon(player_name, carbon):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE player SET carbon = %s WHERE player_name = %s
            """, (carbon, player_name))
            conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()

@sql_blueprint.route('/update_shark/<player_name>/<shark>', methods=['PUT'])
def update_shark(player_name, shark):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE player SET shark = shark + %s WHERE player_name = %s
            """, (shark, player_name))
            conn.commit()
            json = {"message": "Shark updated"}
            return jsonify(json)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
            

def update_inventory(player_name, inventory):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE player SET inventory = %s WHERE player_name = %s
            """, (inventory, player_name))
            conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()

def update_location(player_name, icao):
    cursor = None
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE player SET location_id = %s WHERE player_name = %s
            """, (icao, player_name))
            conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()

@sql_blueprint.route('player_stats/<player_name>')
def player_stats(player_name):
    cursor = None
    try:
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
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()

@sql_blueprint.route('/fly/<airport_type>')
def fly(airport_type):
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name, iso_country, type, ident, latitude_deg, longitude_deg 
            FROM airport 
            WHERE continent = 'EU' AND type = %s AND name NOT LIKE '%?%' 
            ORDER BY RAND() LIMIT 1;
        """, (airport_type,))
        location = cursor.fetchone()  # Use fetchone() for a single row
        
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
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()  # Explicitly close the cursor



initial_setup()


