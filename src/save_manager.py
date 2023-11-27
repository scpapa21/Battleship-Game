import os
import pickle
import pathlib
import pandas as pd

from board import Board


class SaveManager:
    def __init__(self, game_name : str):
        self.game_name = game_name
        self.memory_path = pathlib.Path(__file__).parent.parent / 'data' /'Memory'
        self.game_name_path = self.memory_path / self.game_name 

        # Class Paths
        self.board1_setup_name = str(self.game_name.split()[0]) + ' Setup.pickle'
        self.board1_setup_path = self.game_name_path / self.board1_setup_name 
        
        self.board2_setup_name = str(self.game_name.split()[2]) + ' Setup.pickle'
        self.board2_setup_path = self.game_name_path / self.board2_setup_name 

        self.board1_name = str(self.game_name.split()[2]) + ' Board.pickle'
        self.board1_path = self.game_name_path / self.board1_name 

        self.board2_name = str(self.game_name.split()[2]) + ' Board.pickle'
        self.board2_path = self.game_name_path / self.board2_name 

        # Maps CSV Paths
        self.map1_setup_name = str(self.game_name.split()[0]) + ' Setup Map.csv'
        self.map1_setup_path = self.game_name_path / self.map1_setup_name 
        
        self.map2_setup_name = str(self.game_name.split()[2]) + ' Setup Map.csv'
        self.map2_setup_path = self.game_name_path / self.map2_setup_name 

        self.map1_name = str(self.game_name.split()[2]) + ' Map.csv'
        self.map1_path = self.game_name_path / self.map1_name 

        self.map2_name = str(self.game_name.split()[2]) + ' Map.csv'
        self.map2_path = self.game_name_path / self.map2_name 


    def check_if_game_exists(self):
        dir_list = os.listdir(self.memory_path)
        if self.game_name in dir_list:
            return True
        
        return False


    def check_if_game_is_being_played(self):
        dir_list = os.listdir(self.game_name_path)
        if self.board1_path in dir_list and self.board1_path in dir_list:
            return True
        
        return False
    

    def create_game_folder(self):
        os.mkdir(self.game_name_path)
    

    def delete_game_folder(self):
        pass


    def save_boards(self, board1 : Board, board2 : Board, is_setup : bool):
        if not self.check_if_game_exists():
            self.create_game_folder()

        if is_setup:
            pickle.dump(board1, file = open(self.board1_setup_path, "wb"))
            pickle.dump(board2, file = open(self.board2_setup_path, "wb"))

            board1_setup_df = pd.DataFrame(board1.map)
            board1_setup_df.to_csv(self.map1_setup_path, index=False, header=False)

            board2_setup_df = pd.DataFrame(board2.map)
            board2_setup_df.to_csv(self.map2_setup_path, index=False, header=False)

        else:
            pickle.dump(board1, file = open(self.board1_path, "wb"))
            pickle.dump(board2, file = open(self.board2_path, "wb"))

            board1_df = pd.DataFrame(board1.map)
            board1_df.to_csv(self.map1_path, index=False, header=False)

            board2_df = pd.DataFrame(board2.map)
            board2_df.to_csv(self.map2_path, index=False, header=False)


    def load_boards(self, is_setup : bool):
        if is_setup:
            board1 = pickle.load(open(self.board1_setup_path, "rb"))
            board2 = pickle.load(open(self.board2_setup_path, "rb"))
        else:
            board1 = pickle.load(open(self.board1_path, "rb"))
            board2 = pickle.load(open(self.board2_path, "rb"))
        
        return board1, board2

