
import streamlit as st
import pandas as pd
import random
import time
import joblib

from utils.feature_extraction import extract_features
from game.mindmaze import MindMazeGame

# Load ML model
model = joblib.load("ml_model/mindmaze_difficulty_predictor.pkl")

st.set_page_config(page_title="MindMaze 🧠", layout="centered")
st.title("🧩 MindMaze – Your Daily Brain Circuit")

# Game config
size = st.slider("Maze Size", 3, 8, 5)
if st.button("Generate Maze"):
    game = MindMazeGame(size=size)
    st.session_state["maze"] = game.board
    st.session_state["start_time"] = time.time()

# Display maze
if "maze" in st.session_state:
    st.subheader("🧠 Your Maze")
    for row in st.session_state["maze"]:
        st.markdown(" ".join(f"`{cell}`" for cell in row))

    if st.button("I'm Done Solving"):
        end_time = time.time()
        time_taken = round(end_time - st.session_state["start_time"], 2)
        st.success(f"⏱️ Time to solve: **{time_taken} seconds**")

        # Extract features and predict
        features = extract_features(st.session_state["maze"])
        features["time_to_solve"] = time_taken
        st.write("🔍 Extracted Features", features)

        input_df = pd.DataFrame([{
            "size": features["size"],
            "wall_count": features["wall_count"],
            "path_length": features["path_length"]
        }])

        prediction = model.predict(input_df)[0]
        st.info(f"🧠 Predicted Difficulty: **{prediction.upper()}**")

        # Log it
        log_df = pd.DataFrame([features])
        log_df.to_csv("data/gameplay_log.csv", mode='a', index=False, header=False)

else:
    st.warning("Click 'Generate Maze' to begin.")
