from sql import (create_player, update_money, update_inventory,
                 update_carbon, update_shark)
from utilities import anim_print


class Player:
    def __init__(self, name, balance, carbon, shark, airport_name, airport_country, airport_type):
        self.name = name
        self.balance = balance
        self.carbon = carbon
        self.shark = shark
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
    def display_status(self): # This is pointless will be removed later
        anim_print(f"""
You are at {self.airport_name}, {self.airport_country}.
You have {self.carbon} Carbon and {self.balance}€ in the bank.
""")