from requests import get 
import json
import requests
from PIL import Image 
from io import BytesIO 
from menu import Menu
import sys
import webbrowser

API_KEY = "jXk5dAfV0cxXW5Bjv1eNu3gdGqRYZZKhCEPuoiRC"

""" Retrieves photo from url

Raises:
    RequestionException Error: If image is unidentified.

"""
def display_photo(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.show()
        print("Image displayed successfully")
    except (requests.exceptions.RequestException, Image.UnidentifiedImageError) as e:
        print(f"Error displaying image: {e}")

"""
Used to retrieve the rover selected by the user

Returns: Name of the rover selected.

"""
def get_rover_menu(name):
    print()
    print("Please select a rover from the list:")
    print("1: Opportunity")
    print("2: Spirit")
    print("3: Perserverance")
    print("4: Curiosity")

    rover_input = (int(input("Select rover: ")))

    if rover_input == 1:
        name = "Opportunity"
        print("Opportunity")
    elif rover_input == 2:
        name = "Spirit"
        print("Spirit")
    elif rover_input == 3:
        name = "Perserverance"
        print("Perserverance")
    elif rover_input == 4:
        name = "Curiosity"
        print("Curiosity")
    else: 
        print("Invalid option, please enter again")
        return 
    
    return name

""" Retrieves the sol date inputted by the user

Return: Returns the clients input value.

"""
def get_sol_date():
    user_input = (int(input("Enter Sol Date: ")))
    return user_input

"""Used to exit program"""
def exit():
    sys.exit()

"""Retrieves the image url information based on the users input for rover selection.

Returns:  Returns the image url 

Raises:
    RequestException: If fetch was unsuccessful in retrieving the image

    ValueError: If an incorrect value is provided then what is available to be selected

"""
def fetch_image_urls():
    try:
        rover_choice = get_rover_menu(__name__)
        sol_date = get_sol_date()

        url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_choice}/photos?sol={sol_date}&api_key={API_KEY}"

        response = requests.get(url_rovers)
        response.raise_for_status()
        data = response.json()

        photos = data.get('photos', [])
        if not photos:
            print("No images available")
            return              
        
        image_urls =[photo.get('img_src') for photo in photos[:10] if photo.get('img_src')]
        return image_urls
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    except ValueError as e:
        print(e)
        return

""" Displays the rover photo from the selection made by the user.

Raises:
    webbrowser.Error:  Raise when image is not able to be loaded in the current browser

"""
def display_rover_photos(image_urls):
    num_images = len(image_urls)
    current_index = 0

    while True:
        print(f"\n Photo View (Photo {current_index +1} of {num_images})")
        rover_image_url = image_urls[current_index]
        print(f"Attempting to open URL: {rover_image_url}")
        
        try:
            webbrowser.open_new_tab(rover_image_url)
        except webbrowser.Error as e:
            print(f"Could not open image in browser: {e}")
        
        print("\nNavigation: 'n' (Next), 'p' (Previous), 'm' (Main Menu)")
        user_input = input("Enter your choice: ").lower()
        
        if user_input == 'n':
            current_index = (current_index + 1) % num_images
        elif user_input == 'p':
            current_index = (current_index - 1 + num_images) % num_images
        elif user_input == 'm':
            return
        else:
            print("Invalid command. Please use 'n', 'p', or 'm'.")

"""Handles the main operation of the application and menu options provided"""
def main():
    while True:
        print("Mars Rover Photos")
        print("1. View Rover Photos")
        print("2. Exit")
        choice = input ("Enter your choice: ")

        if choice == '1':
            image_urls = fetch_image_urls()
            if image_urls:
                display_rover_photos(image_urls)
        elif choice == '2':
            print("Exiting Program")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
