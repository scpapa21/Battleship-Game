import numpy as np
import ships as shp

class Board:
    def __init__(self, ships : dict, player_name : str):
        self.empty_board = [['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0'],
                            ['0','0','0','0','0','0','0','0','0','0']]
        
        self.map = np.array(self.empty_map)
        self.enemy_map = np.array(self.empty_map)

        self.player = player_name
        self.ships = ships
        self.placed_ships = []

        self.files = list('ABCDEFGHIJ')
        

    def see_player_map(self):
        print(f"\n{self.player}'s map:")

        column_info = '  |'
        for index in range(1,len(self.files) + 1):
            column_info += ' ' + str(index) + ' |'
        print(column_info.rstrip('|'))

        print('-' * 42)
        for index, file in enumerate(self.map):
            file_info = self.files[index] + ' |'
            for column in file:
                file_info += ' ' + str(column) + ' |'
            print(file_info.rstrip('|'))
            print('-' * 42)

    
    def see_enemy_map(self):
        print(self.enemy_map)

    
    def place_ships(self):
        for ship in self.ships:
            size = self.ships[ship]['size']
            print(f'Ship to place: {ship}\nSize of this ship: {size}')

            self.see_player_map()

            ship_position_info = self.__ask_player_for_position()
            position_to_place = ship_position_info[0]
            direction = ship_position_info[1]
            
            while not self.__position_is_empty(size,position_to_place,direction):
                print("The position you entered is invalid!❌\nCheck the map and the ship size to make sure to select a valid position!")
                ship_position_info = self.__ask_player_for_position()
                position_to_place = ship_position_info[0]
                direction = ship_position_info[1]
            
            self.__place_ship(ship,position_to_place,direction)


    def ships_summary(self):
        print("After your enemy's turn this is a summary of your ships health:\n")
        for ship in self.placed_ships:
            self.__give_ship_summary(ship)
    
    # Place Ships Methods
    def __ask_player_for_position(self):
        position = input('Enter this ship starting position: (Example: A1)')
        position_to_place = [self.files.index(position[0]), int(position[1:]) - 1]

        direction = input('In which direction you want to place it? H or V?')

        return position_to_place, direction

    def __place_ship(self, ship : str,  position_to_place : list, direction : str):
        size = self.ships[ship]['size']

        file_to_place = position_to_place[0]
        column_to_place = position_to_place[1]

        if direction == 'H':
            self.map[file_to_place][column_to_place:column_to_place + size] = ship[0]
        elif direction == 'V':
            self.map.T[column_to_place][file_to_place:file_to_place + size] = ship[0] 
        
        self.__add_to_placed_ships(ship)

        print(f'Great!! Your {ship} was correctly placed!✅\n')

    def __position_is_empty(self, ship_size : int, position_to_place : list, direction : str):
        count_available = 0
        start_check = False

        if direction == 'H':
            array = self.map
            file = 0
            column = 1
        elif direction == 'V':
            array = self.map.T
            file = 1
            column = 0

        for index, square in enumerate(array[position_to_place[file]]):
                if index == position_to_place[column]:
                    start_check = True
                
                if start_check:
                    if square == '0':
                        count_available += 1
                    else:
                        return False
                
                if count_available == ship_size:
                    return True
            
        return False

    def __add_to_placed_ships(self, ship_name : str):
        size = self.ships[ship_name]['size']

        ship = shp.Ship(ship_name, size)
        ship.ship_gets_placed()
        self.placed_ships.append(ship)


    # Ships Summary Methods
    def __give_ship_summary(self, ship : shp.Ship):
        ship.display_information()
