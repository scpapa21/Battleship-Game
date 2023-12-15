from board import Board
from save_manager import SaveManager


ships = {'Carrier': {'size' : 5}, 
         'Battleship' : {'size' : 4},
         'Destroyer': {'size': 3},
         'Submarine': {'size': 3},
         'Patrol Boat': {'size': 2}}


class BattleshipGame:
    def __init__(self, player1_name : str, player2_name :str):
        self.player1 = player1_name
        self.player2 = player2_name
        self.game_name = self.player1 + ' vs ' + self.player2

        self.player_turn = player1_name
        self.game_turn = 1
        self.game_completed = False

        self.players_boards = {self.player1 : Board(ships, self.player1), self.player2 : Board(ships, self.player2)}

        self.save_manager = SaveManager(self.game_name)
    
    
    def start_game(self):
        print('Welcome to Battleship in Ptyhon!! ⚓⛵🚢\n')
        if self.save_manager.check_if_game_exists():
            if self.save_manager.check_if_game_is_being_played():
                self.load_game()
                print('Loading Game ...')
                print('Game Loaded!! Please continue your game!\nBombs Away 💣💣💣\n')
                return
                
            else:
                load_setup = input('Do you want to use your previous Ships Setup? Y or N?\n')

                if load_setup == 'N':
                    self.setup_game()
                elif load_setup == 'Y':
                    self.load_setup()

        else:
            self.setup_game()
        
        print('Setup Ready!😎')
        print('Fantastic! Now let the game begin!\nBombs Away 💣💣💣\n')
        self.player_plays()


    def setup_game(self):
        print(f'{self.player1} will start! 🎉\nPlease place all your ships!\n')
        self.players_boards[self.player1].place_ships()

        print(f'Now is turn for {self.player2} to place ships!')
        self.players_boards[self.player2].place_ships()
        
        self.save_setup()
    

    def player_plays(self):
        self.turn_active = True
        self.players_boards[self.player_turn].ships_summary()

        while self.turn_active:
            option = self.__ask_player_for_turn_selection()

            if option == 1:
                self.players_boards[self.player_turn].see_player_map()
            elif option == 2:
                self.players_boards[self.player_turn].see_enemy_map()
            else:
                self.__ask_where_to_shoot()

        self.__change_turn()


    def __check_winner(self):
        pass


    def __ask_player_for_turn_selection(self):
        print(f"\nIt's your turn {self.player_turn}!!\nWhat do you want to do?")
        print("1. See my board\n2. See my enemy's board\n3. Shoot!!🫡")

        option = input('\nEnter the option you want: (Please just enter the option number)')

        return self.__check_valid_option(option)


    def __check_valid_option(self, option):
        valid = option in ['1','2','3','1.','2.','3.']

        while not valid:
            print("The option you entered is invalid!❌")
            option = input('\nEnter the option you want: (Please just enter the option number)')
            valid = option in ['1','2','3','1.','2.','3.']
        
        option = int(option.replace('.',''))
        
        return option


    def __ask_where_to_shoot(self):
        pass

        
    def __change_turn(self):
        if self.player_turn == self.player1:
            self.player_turn = self.player2
        elif self.player_turn == self.player2:
            self.player_turn = self.player1
        
        self.game_turn += 1


    # Save Manager methods
    def save_setup(self):
        self.save_manager.save_boards(self.players_boards[self.player1], self.players_boards[self.player2], True)
    

    def save_game(self):
        self.save_manager.save_boards(self.players_boards[self.player1], self.players_boards[self.player2].board, False)
    

    def load_setup(self):
        boards = self.save_manager.load_boards(True)
        self.players_boards[self.player1] = boards[0]
        self.players_boards[self.player2] = boards[1]
    
    
    def load_game(self):
        boards = self.save_manager.load_boards(False)
        self.players_boards[self.player1] = boards[0]
        self.players_boards[self.player2] = boards[1]
    

if __name__ == '__main__':
    game = BattleshipGame('Santi', 'Vane')
    game.start_game()
