
from game.mindmaze import MindMazeGame
from utils.feature_extraction import extract_features
import pandas as pd

game = MindMazeGame(size=5)
game.start_game()
time_taken = game.time_to_solve()
print(f"Time to solve: {time_taken} seconds")

features = extract_features(game.board)
features["time_to_solve"] = time_taken

# Log gameplay for future ML use
df = pd.DataFrame([features])
df.to_csv("data/gameplay_log.csv", mode='a', index=False, header=False)
