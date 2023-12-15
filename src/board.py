import numpy as np
from ships import Ship

class Board:
    def __init__(self, ships : dict, player_name : str):
        self.empty_map =   [['0','0','0','0','0','0','0','0','0','0'],
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
        self.enemy_map = self.__modify_sea_squares()

        print("\nYour enemy's map:")

        column_info = '  |'
        for index in range(1,len(self.files) + 1):
            column_info += '  ' + str(index) + '  |'
        print(column_info.rstrip('|'))

        print('-' * 62)
        for index, file in enumerate(self.enemy_map):
            file_info = self.files[index] + ' |'
            for column in file:
                file_info += '  ' + str(column) + ' |'
            print(file_info.rstrip('|'))
            print('-' * 62)
        
    
    def place_ships(self):
        for ship in self.ships:
            size = self.ships[ship]['size']
            print(f'Ship to place: {ship}\nSize of this ship: {size}')

            self.see_player_map()

            ship_position_info = self.__ask_player_for_position()
            position_to_place = ship_position_info[0]
            direction = ship_position_info[1]
            
            while not self.__position_is_empty(size,position_to_place,direction):
                print("\nThe position you entered is invalid!❌\nCheck the map and the ship size to make sure to select a position that's empty and that the ship fits!")
                ship_position_info = self.__ask_player_for_position()
                position_to_place = ship_position_info[0]
                direction = ship_position_info[1]
            
            self.__place_ship(ship,position_to_place,direction)


    def ships_summary(self):
        print("This is a summary of your ships health after your enemy's turn:\n")
        for ship in self.placed_ships:
            self.__give_ship_summary(ship)
    

    # Place Ships Methods
    def __ask_player_for_position(self):
        while True:
            position = input('Enter this ship starting position: (Example: A1)')
            if (not self.__check_valid_character(position[0], 'letter') or not self.__check_valid_character(position[1:], 'number')):
                print('\nInvalid Position! ❌\nYou entered an invalid character! First character must be a letter followed by a number!')
                continue

            letter = position[0]
            number = int(position[1:]) - 1

            if not self.__check_valid_position(letter, number):
                print('\nInvalid Position! ❌\nThe position you entered is not part of the map, please check the map and enter a position that is part of it!')
                continue

            letter_index = self.files.index(letter.upper())
            position_to_place = [letter_index, number]

            direction = input('In which direction do you want to place it? H or V?')
            if direction.upper() not in ['H', 'V']:
                print('\nInvalid direction! ❌\nPlease enter either H (horizontal) or V (vertical).')
                continue

            return position_to_place, direction.upper()


    def __check_valid_character(self, character, letter_or_number : str):
        if letter_or_number == 'letter':
            return character.isalpha()
        
        if letter_or_number == 'number':
            return character.isdigit()


    def __check_valid_position(self, letter : str, number : int):
        if letter.upper() not in self.files:
            return False
        
        if number not in [0,1,2,3,4,5,6,7,8,9]:
            return False
        
        return True
    

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

        ship = Ship(ship_name, size)
        ship.ship_gets_placed()
        self.placed_ships.append(ship)
    

    # Map Visualization Methods
    def __modify_sea_squares(self):
        new_row = []
        new_map = []

        for row in self.enemy_map:
            for square in row:
                if square == '0':
                    new_row.append('🌊')
                else:
                    new_row.append(square)
            
            new_map.append(new_row)
            new_row = []
        
        return np.array(new_map)


    # Ships Summary Methods
    def __give_ship_summary(self, ship : Ship):
        ship.display_information()


if __name__ == '__main__':
    ships = {'Carrier': {'size' : 5}, 
         'Battleship' : {'size' : 4},
         'Destroyer': {'size': 3},
         'Submarine': {'size': 3},
         'Patrol Boat': {'size': 2}}
    
    board = Board(ships, 'Vane')
    board.see_enemy_map()
