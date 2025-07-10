import json
import re
from collections import defaultdict

# Function to read spritesheet coordinates, giving the start and end frames
def read_coordinates(json_path):
    # Open given file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Get each frame
    frames = data.get("frames", {})

    # Set up a list of animations
    animations = defaultdict(list)

    # Go through each frame in the file and get coordinates for each
    for filename, frame_data in frames.items():
        # Strip file extensions
        name = filename.replace(".png", "")
        match = re.match(r"([A-Za-z]+(?:[A-Z][a-z]+)*)(\d+)?$", name)

        # Match any groups (frames with same name but different number)
        if match:
            prefix = match.group(1)
            number = int(match.group(2)) if match.group(2) else 0
            coords = frame_data["frame"]
            # Store each in list
            animations[prefix].append((number, coords, filename))


    # Display all frames and their coordinates
    for anim, coords in animations.items():
        # Sort by frame number, getting the first and last frames
        sorted_coords = sorted(coords, key=lambda x: x[0])
        first_frame = sorted_coords[0]
        last_frame = sorted_coords[-1]
        # Display all start and end coordinates
        print(f"{anim}XStart =", first_frame[1]["x"], f"{anim}YStart =", first_frame[1]["y"])
        print(f"{anim}XEnd =", last_frame[1]["x"], f"{anim}YEnd =", last_frame[1]["y"])
        print()

# Call function
read_coordinates("spritesheet.json")