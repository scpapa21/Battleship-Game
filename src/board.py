import numpy as np

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
        
        self.board = np.array(self.empty_board)
        self.enemy_board = np.array(self.empty_board)

        self.player = player_name
        self.ships = ships

        self.files = list('ABCDEFGHIJ')
        

    def see_player_board(self):
        print(f"\n{self.player}'s board:")

        column_info = '  |'
        for index in range(1,len(self.files) + 1):
            column_info += ' ' + str(index) + ' |'
        print(column_info.rstrip('|'))

        print('-' * 42)
        for index, file in enumerate(self.board):
            file_info = self.files[index] + ' |'
            for column in file:
                file_info += ' ' + str(column) + ' |'
            print(file_info.rstrip('|'))
            print('-' * 42)

    
    def see_enemy_board(self):
        print(self.enemy_board)
    
    def place_ships(self):
        for ship in self.ships:
            size = self.ships[ship]['size']
            print(f'Ship to place: {ship}\nSize of this ship: {size}')

            self.see_player_board()

            ship_position_info = self.__ask_player_for_position()
            position_to_place = ship_position_info[0]
            direction = ship_position_info[1]
            
            while not self.__position_is_empty(size,position_to_place,direction):
                print("The position you entered is invalid!❌\nCheck the board and the ship size to make sure to select a valid position!")
                ship_position_info = self.__ask_player_for_position()
                position_to_place = ship_position_info[0]
                direction = ship_position_info[1]
            
            self.__place_ship(ship,position_to_place,direction)


    
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
            self.board[file_to_place][column_to_place:column_to_place + size] = ship[0]
        elif direction == 'V':
            self.board.T[column_to_place][file_to_place:file_to_place + size] = ship[0] 

        print(f'Great!! Your {ship} was correctly placed!✅\n')

    def __position_is_empty(self, ship_size : int, position_to_place : list, direction : str):
        count_available = 0
        start_check = False

        if direction == 'H':
            array = self.board
            file = 0
            column = 1
        elif direction == 'V':
            array = self.board.T
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
