import json
from collections import defaultdict

# Function to read spritesheet coordinates
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
        anim_name = filename
        coords = frame["frame"]
        # Store each in list
        animations[anim_name].append({
            "x": coords["x"],
            "y": coords["y"]
        })

    # Display all frames and their coordinates
    for anim, coords in animations.items():
        x = min(c["x"] for c in coords)
        y = min(c["y"] for c in coords)

        print(f"{anim}:")
        print(f" Frame: ({x}, {y})")
        print()

# Call function
read_coordinates("spritesheet.json")