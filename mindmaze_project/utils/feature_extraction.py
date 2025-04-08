
def extract_features(board):
    size = len(board)
    wall_count = sum(row.count('X') for row in board)
    path_length = size * 2 - 2  # Simplified placeholder
    return {"size": size, "wall_count": wall_count, "path_length": path_length}
