import os
import pathlib
import pandas as pd

class SaveManager:
    def __init__(self, game_name : str):
        self.game_name = game_name
        self.memory_path = pathlib.Path(__file__).parent.parent / 'data' /'Memory'
        self.game_name_path = self.memory_path / self.game_name 

        self.board1_setup_name = str(self.game_name.split()[0]) + ' Setup.csv'
        self.board1_setup_path = self.game_name_path / self.board1_setup_name 
        
        self.board2_setup_name = str(self.game_name.split()[2]) + ' Setup.csv'
        self.board2_setup_path = self.game_name_path / self.board2_setup_name 

        self.board1_name = str(self.game_name.split()[2]) + ' Board.csv'
        self.board1_path = self.game_name_path / self.board1_name 

        self.board2_name = str(self.game_name.split()[2]) + ' Board.csv'
        self.board2_path = self.game_name_path / self.board2_name 

    def check_if_game_exists(self):
        dir_list = os.listdir(self.memory_path)
        if self.game_name in dir_list:
            return True
        
        return False

    def create_game_folder(self):
        os.mkdir(self.game_name_path)
    
    def delete_game_folder(self):
        pass

    def save_boards(self, board1 : list, board2 : list, is_setup : bool):
        if not self.check_if_game_exists():
            self.create_game_folder()

        if is_setup:
            board1_setup_df = pd.DataFrame(board1)
            board1_setup_df.to_csv(self.board1_setup_path, index=False, header=False)

            board2_setup_df = pd.DataFrame(board2)
            board2_setup_df.to_csv(self.board2_setup_path, index=False, header=False)
        else:
            board1_df = pd.DataFrame(board1)
            board1_df.to_csv(self.board1_path, index=False, header=False)

            board2_df = pd.DataFrame(board2)
            board2_df.to_csv(self.board2_path, index=False, header=False)

    def load_boards(self, is_setup : bool):
        if is_setup:
            board1 = pd.read_csv(self.board1_setup_path).values.tolist()
            board2 = pd.read_csv(self.board2_setup_path).values.tolist()
        else:
            board1 = pd.read_csv(self.board1_path).values.tolist()
            board2 = pd.read_csv(self.board2_path).values.tolist()
        
        return board1, board2

