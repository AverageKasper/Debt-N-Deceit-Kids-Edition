from python_app.routes.sql import (create_player, update_money, update_inventory,
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
        self.is_alive = True
        self.death_reason = None
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

    def death(self, reason):
        self.is_alive = False
        self.death_reason=reason

        print(f"{self.name} has lost. Reason: {reason}")


    def validate_bet(self, bet):
        if not self:
            raise ValueError("No player here bozo")
        if bet<=0:
            return {"Error": "Bet must be greater than zero"}
        if bet>self.balance:
            return {"Error": "Insufficient funds"}
        return None
    
# Temp Player for testing
#player = Player('test', 1000, 100, 0, 0, 'Helsinki-Vantaa', 'Finland', 'large_airport')
player=None
# Player none doesnt need to be here (in theory) because when you run the game the player object is created at the start
# This fixes some bullshit error in pycharm
def create_player_object(player_name, money, carbon, shark, inventory, airport_name, airport_country, airport_type):
    global player
    player = Player(player_name, money, carbon, shark, inventory, airport_name, airport_country, airport_type)
    return player