from sql import (create_player, update_money, update_inventory,
                 update_carbon, update_shark)



class Player:
    def __init__(self, name, balance, carbon, shark, inventory, airport_name, airport_country, airport_type):
        self.name = name
        self.balance = balance
        self.carbon = carbon
        self.shark = shark
        self.inventory = inventory
        self.airport_name = airport_name
        self.airport_country = airport_country
        self.airport_type = airport_type
        create_player(self.name, self.balance, self.carbon, self.shark)


    def update_location(self, airport_name, airport_country, airport_type):
        self.airport_name = airport_name
        self.airport_country = airport_country
        self.airport_type = airport_type

    def update_balance(self, amount):
        self.balance += amount
        update_money(self.name, self.balance)

    def update_carbon(self, amount):
        self.carbon += amount
        update_carbon(self.name, self.carbon)

    def update_shark(self, amount):
        self.shark += amount
        update_shark(self.name, self.shark)
    
    def update_inventory(self, amount):
        self.inventory += amount
        update_inventory(self.name, self.inventory)
    
    
# Temp Player for testing
#player = Player('test', 1000, 100, 0, 0, 'Helsinki-Vantaa', 'Finland', 'large_airport')
player = None
def create_player_object(player_name, money, carbon, shark, inventory, airport_name, airport_country, airport_type):
    global player
    player = Player(player_name, money, carbon, shark, inventory, airport_name, airport_country, airport_type)
    return player