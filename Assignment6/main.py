import os
import time
import urllib.request
import json
import climage
import requests
from io import BytesIO
from PIL import Image

#menus
def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("POKETOOL")
    print("Welcome to the PokeTool!")
    print("You can use this tool to find information about Pokemon, their moves, and items from the Pokemon games!\n")
    print("Please select one of the following options and follow the instructions.")
    print("You have 4 options:")
    print("1. Type the value '1' into the command line to search specifically for Pokemon")
    print("2. Type the value '2' into the command line to search specifically for items")
    print("3. Type the value '3' into the command line to search specifically for Pokemon moves")
    print("4. Type the value '4' into the command line to quit the program")

def poke_search_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("POKETOOL\n")
    print("POKEMON SEARCH")
    print("Welcome to the Pokemon Search!")
    print("You can use this to find more information about specific Pokemon!\n")
    print("Please select one of the following options and follow the instructions.")
    print("You have 3 options:")
    print("1. Type the value '1' into the command line to search for a Pokemon name or Pokedex number")
    print("2. Type the value '2' into the command line to view a random Pokemon")
    print("3. Type the value '3' into the command line to return to the previous page")

def item_search_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("POKETOOL\n")
    print("ITEM SEARCH")
    print("Search for Items!")
    print("You can use this to find more information about specific Items!\n")
    print("Please select one of the following options and follow the instructions.")
    print("You have 3 options:")
    print("1. Type the value '1' into the command line to search for a Item name or a Item ID")
    print("2. Type the value '2' into the command line to view a random Item")
    print("3. Type the value '3' into the command line to return to the previous page")

def move_search_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("POKETOOL\n")
    print("MOVE SEARCH")
    print("Search for Moves!")
    print("You can use this to find more information about specific Moves!\n")
    print("Please select one of the following options and follow the instructions.")
    print("You have 3 options:")
    print("1. Type the value '1' into the command line to search for a Move name or a Move ID")
    print("2. Type the value '2' into the command line to view a random Move")
    print("3. Type the value '3' into the command line to return to the previous page")

def poke_search():
    while True:
        poke_search_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            while True:
                search_term = input("Enter in a Pokemon name or Pokemon number: ")
                try:
                    req = urllib.request.Request('https://pokeapi.co/api/v2/pokemon/'+str(search_term), headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        # Read the response data
                        data = response.read().decode('utf-8')
                        pokemon_data = json.loads(data)
                        # Print the response data
                        name = pokemon_data["species"]["name"]
                        image = pokemon_data["sprites"]["front_default"]
                        response = requests.get(image)
                        image_data = BytesIO(response.content)
                        # Display the image
                        a = climage.convert(image_data)
                        print(a)
                        print("POKEMON NAME: "+ str(name))
                        #seperate image
                        # i = Image.open(image_data)
                        # i.show()
                except urllib.error.URLError as e:
                        print('Error:', e.reason)
                break
        elif choice == '2':
            break
        elif choice == '3':
            print("Returning to the previous page!")
            break
        else:
            print("You entered '"+ str(choice) + "' as the input. Please follow the instructions for the different options and enter a number between 1 and 3.")
        input("Press Enter to continue...")

def item_search():
    while True:
        item_search_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
                break
        elif choice == '2':
            break
        elif choice == '3':
            print("Returning to the previous page!")
            break
        else:
            print("You entered '"+ str(choice) + "' as the input. Please follow the instructions for the different options and enter a number between 1 and 3.")
        input("Press Enter to continue...")

def move_search():
    while True:
        move_search_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
                break
        elif choice == '2':
            break
        elif choice == '3':
            print("Returning to the previous page!")
            break
        else:
            print("You entered '"+ str(choice) + "' as the input. Please follow the instructions for the different options and enter a number between 1 and 3.")
        input("Press Enter to continue...")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            poke_search()
        elif choice == '2':
            item_search()
        elif choice == '3':
            move_search()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("You entered '"+ str(choice) + "' as the input. Please follow the instructions for the different options and enter a number between 1 and 4.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
