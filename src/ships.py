class Ship:
    def __init__(self, name, size):
        self.name = name
        self.initial_health = size
        self.current_health = self.initial_health

        self.placed = False
        self.destroyed = False

    def display_information(self):
        life_percentage = (self.current_health // self.initial_health) * 100

        if life_percentage == 0:
            print(f'The {self.name} has been destroyed! 😵😢😵')
        elif life_percentage <= 30:
            print(f'Your {self.name} is about to be destroyed! 😰😰 It only has {life_percentage}% health remaining!')
        else:
            print(f'Your {self.name} has {life_percentage}% health remaining!')

    def ship_gets_placed(self):
        self.placed = True

    def gets_hit(self):
        self.current_health -= 1

        if self.current_health == 0:
            self.destroyed = True
