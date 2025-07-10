# How to run
Run the main.py file as you would run any Python file (python -u "main.py") so long as you are in the correct directory.  Once it is running you will be given two options one designed for json files from TexturePacker Online the other for json files from Texture Atlas Generator (They make work with other similar json data files).

The file will read from spritesheet.json, to use your own file just replace the example spritesheet.json file with your own, keep the name "spritesheet.json".

# About the app
I made this to make it easier to store start and end coordinate values for animations in my game when I change the spritesheet.

It reads from a json data file, similar to ones you would get from sites such as TexturePacker when making custom spritesheets. The json file should store the coordinates of each frame/texture in the spritesheet, this program will read out the start and end coordinates for each texture using numbers to do so. An example would be if there are 6 textures named sprint1, sprint2, sprint, etc it will get the coordinates for sprint 1 and sprint 6 allowing you to use these values in your own program for iterating through animation frames.

There are two options available, one is designed for TexturePacker Online (the free one) by codeandweb, the other is designed for Texture Atlas Generator by Umesh-KC but it will also work on similar json files. There is also a file designed for the Texture Atlas Generator which lists the coordinate values for every texture.