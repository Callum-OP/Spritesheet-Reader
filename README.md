# How to run
Just open the site on the index page (https://callum-op.github.io/Spritesheet-Reader/) and enter your desired json data file, it will automatically give output.

# About the app
I made this to make it easier to store start and end coordinate values for animations in my game when I change the spritesheet.

It reads from a json data file, similar to ones you would get from sites such as TexturePacker when making custom spritesheets. The json file should store the coordinates of each frame/texture in the spritesheet, this program will read out the start and end coordinates for each texture using numbers to do so. An example would be if there are 6 textures named sprint1, sprint2, sprint, etc it will get the coordinates for sprint 1 and sprint 6 allowing you to use these values in your own program for iterating through animation frames.

I have changed the code from Python to JavaScript to make it easier to host so that I can access this site much more easily when I need it. I have included the old files in a seperate folder.

# Example Output
<img width="1867" height="868" alt="image" src="https://github.com/user-attachments/assets/2652d27f-d1b0-4582-84b8-256f19f0a2c4" />
<img width="1867" height="868" alt="image" src="https://github.com/user-attachments/assets/5b5b0cb3-5cb4-44fe-a8b0-4cde8df13dbd" />



