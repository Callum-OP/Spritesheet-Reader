import json
import re
from collections import defaultdict

# Function to read spritesheet coordinates, giving the start and end frames
def read_coordinates(json_path):
    # Open given file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Get each frame
    texture = data.get("textures", [])[0]
    frames = texture.get("frames", [])

    # Set up a list of animations
    animations = defaultdict(list)

    # Go through each frame in the file and get coordinates for each
    for frame in frames:
        filename = frame["filename"]
        match = re.match(r"([A-Za-z]+)([A-Za-z]*)(\d+)?$", filename)

        # Match any groups (frames with same name but different number)
        if match:
            prefix = match.group(1) + match.group(2)
            number = int(match.group(3)) if match.group(3) else 0
            # Store each in list
            animations[prefix].append((number, frame["frame"], filename))

    # Function to display all coordinates
    def format_coords(entry):
        frame = entry[1]
        return {
            "x": frame["x"],
            "y": frame["y"]
    }

    # Display all frames and their coordinates
    for anim, coords in animations.items():
        # Sort by frame number, getting the first and last frames
        sorted_coords = sorted(coords, key=lambda x: x[0])
        first_frame = sorted_coords[0]
        last_frame = sorted_coords[-1]

        print(f"{anim}:")
        print("  First Frame:", format_coords(first_frame))
        print("  Last Frame: ", format_coords(last_frame))
        print()

# Call function
read_coordinates("spritesheet.json")