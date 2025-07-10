# How to run
Run the file as you would run any Python file (python -u "frameReader.py") so long as you are in the correct directory. The file will read from spritesheet.json, to use your own file just replace the example spritesheet json file with your own keeping the name "spritesheet.json".

# About the app
It reads from a json data file, similar to ones you would get from sites such as TexturePacker when making custom spritesheets. The json file should store the coordinates of each frame/texture in the spritesheet, this program will read out the start and end coordinates for each texture using numbers to do so. An example would be if there are 6 textures named sprint1, sprint2, sprint, etc it will get the coordinates for sprint 1 and sprint 6 allowing you to use these values 