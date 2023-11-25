ships = {'Carrier': {'size' : 5}, 
         'Battleship' : {'size' : 4},
         'Destroyer': {'size': 3},
         'Submarine': {'size': 3},
         'Patrol Boat': {'size': 2}}

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.initial_health = size
        self.current_health = self.initial_health

        self.placed = False
        self.destroyed = False

    def display_information(self):
        life_percentage = (self.current_health / self.initial_health) * 100
        print(f'This {self.name} has {life_percentage}% health remaining!')

    def ship_gets_placed(self):
        self.placed = True

    def gets_hit(self):
        self.current_health -= 1

        if self.current_health == 0:
            self.destroyed = True
