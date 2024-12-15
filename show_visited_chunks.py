import os
import re
import matplotlib.pyplot as plt
import sys

def show_visited_chunks(directory):
    pattern = r"world_(-?\d+)_(-?\d+)\.png_petri"
    chunk_coordinates = []

    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            x, y = map(int, match.groups())
            chunk_coordinates.append((x // 512, -y // 512))

    if chunk_coordinates:
        x_chunks, y_chunks = zip(*chunk_coordinates)
    else:
        x_chunks, y_chunks = [], []

    plt.figure(figsize=(10, 8))
    plt.scatter(x_chunks, y_chunks, c="blue", alpha=0.6, edgecolors='w')
    plt.title("Visited Chunks Visualization")
    plt.xlabel("Chunk X Coordinate")
    plt.ylabel("Chunk Y Coordinate")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python show_visited_chunks.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    show_visited_chunks(directory)
