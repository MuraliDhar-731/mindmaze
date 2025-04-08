
import random
import time

class MindMazeGame:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()
        self.start_time = None
        self.end_time = None

    def generate_board(self):
        return [[random.choice(['.', 'X']) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def start_game(self):
        print("Welcome to MindMaze!")
        print("Reach the bottom-right corner from top-left avoiding 'X' (walls)")
        self.display_board()
        self.start_time = time.time()
        input("Press Enter when done solving...")
        self.end_time = time.time()

    def time_to_solve(self):
        return round(self.end_time - self.start_time, 2) if self.end_time and self.start_time else None
