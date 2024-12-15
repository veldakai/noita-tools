import os
import re
import matplotlib.pyplot as plt
import sys

def show_visited_chunks(save_directory_path):
    # Append "world" subdirectory to the given directory path
    directory = os.path.join(save_directory_path, "world")
    pattern = r"world_(-?\d+)_(-?\d+)\.png_petri"
    chunk_coordinates = []

    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            x, y = map(int, match.groups())
            chunk_coordinates.append((x // 512, y // 512))

    if chunk_coordinates:
        x_chunks, y_chunks = zip(*chunk_coordinates)
    else:
        x_chunks, y_chunks = [], []

    plt.figure(figsize=(10, 8))
    plt.scatter(x_chunks, y_chunks, c="blue", alpha=0.6, edgecolors='w')
    plt.title("Visited Chunks Visualization")
    plt.xlabel("Chunk X Coordinate")
    plt.ylabel("Chunk Y Coordinate")

    # Add guiding lines
    plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.axhline(0, color='black', linewidth=1)  # Horizontal center line
    plt.axvline(0, color='black', linewidth=1)  # Vertical center line

    # Set custom ticks for the X-axis
    x_min = min(x_chunks) if x_chunks else -35
    x_max = max(x_chunks) if x_chunks else 35
    x_ticks = list(range((x_min // 70 - 1) * 70 + 35, (x_max // 70 + 1) * 70 + 1, 70))
    plt.xticks(x_ticks)

    # Ensure the Y-axis is inverted (positive Y goes down)
    plt.gca().invert_yaxis()

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python show_visited_chunks.py <save_directory_path>")
        sys.exit(1)
    
    save_directory_path = sys.argv[1]
    show_visited_chunks(save_directory_path)
