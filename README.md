# Noita Tools

A collection of simple tools realted to Noita game.

## Tools
1. **visualize_coords.py**: Visualizes coordinates from filenames with the pattern `world_{x-coord}_{y-coord}.png_petri`.
   - Usage:
     ```sh
     python show_visited_chunks.py /path/to/save/directory
     ```

## Get started
Start working with project
```sh
# make python environment
python -m venv noita-tools
# activate environment
source noita-tools/bin/activate
# install dependencies
pip install -r requirements.txt
```

Stop working with project
```sh
# deactivate environment
deactivate
# remove environment
rm -rf noita-tools
