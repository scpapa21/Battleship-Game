import board as br
import ships as shp
import save_manager as sm


class BattleshipGame:
    def __init__(self, player1_name : str, player2_name :str):
        self.player1 = player1_name
        self.player2 = player2_name

        self.game_name = self.player1 + ' vs ' + self.player2
        self.game_turn = player1_name
        self.game_completed = False

        self.player1_board = br.Board(shp.ships, self.player1)
        self.player2_board = br.Board(shp.ships, self.player2)

        self.save_manager = sm.SaveManager(self.game_name)
    
    
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
        self.player1_board.place_ships()

        print(f'Now is turn for {self.player2} to place ships!')
        self.player2_board.place_ships()
        
        self.save_setup()
    

    def player_plays(self):
        self.player1_board.ships_summary()
        self.player2_board.ships_summary()


    def __check_winner(self):
        pass


    # Save Manager methods
    def save_setup(self):
        self.save_manager.save_boards(self.player1_board, self.player2_board, True)
    

    def save_game(self):
        self.save_manager.save_boards(self.player1_board, self.player2_board.board, False)
    

    def load_setup(self):
        boards = self.save_manager.load_boards(True)
        self.player1_board = boards[0]
        self.player2_board = boards[1]
    
    
    def load_game(self):
        boards = self.save_manager.load_boards(False)
        self.player1_board = boards[0]
        self.player2_board = boards[1]
    

if __name__ == '__main__':
    game = BattleshipGame('Santi', 'Vane')
    game.start_game()
