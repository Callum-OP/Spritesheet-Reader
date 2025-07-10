import subprocess

# Function to access all other functions
def main():
    print("Welcome to Spritesheet Reader")
    print("Choose an option:")
    print("1. Animation Spritesheet Reader - Basic (An example would be json files from TexturePacker Online from codeandweb)")
    print("2. Animation Spritesheet Reader - Standard (An example would be json files from Texture Atlas Generator by Umesh-KC)")
    print("3. Spritesheet Reader - Standard (Designed for json files from Texture Atlas Generator)")
    print("")
    print("The Animation Spritesheet Readers will list the start and end coordinates for groups of textures in the spritesheet")
    print("The Spritesheet Reader will list the coordinates for every texture in the spritesheet")
    print("")

    choice = input("Enter 1 or 2 or 3: ").strip()

    if choice == "1":
        subprocess.run(["python", "basic.py"])
    elif choice == "2":
        subprocess.run(["python", "standard.py"])
    elif choice == "3":
        subprocess.run(["python", "listAll.py"])
    else:
        print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
