from PIL import Image, ImageFile
import random
import glob
import os

def main():

    
    background_img = input("Select your background: \n1) Death City \n2) Hyrule Field \n3) The Moon \n4) Minecraft Cave \n5) Random")
    character_A = input("Select your first character: \n1) Link \n2) Death the Kid \n3) Papa Emeritus II \n4) Perry the Platypus \n5) Random")
    character_B = input("Select your second character: \n1) King Bob \n2) Geralt of Rivia \n3) Foxy \n4) Batman \n5) Random")
    character_pet = input("Select a pet for your characters: \n1) Garfield \n2) Navi \n3) Bolt \n4) Dimple \n5) Random")
    quote_select = input("Would you like to display a randomly generated quote? \nY/N")

    
    os.chdir("bgrounds")
    if background_img == "5":
        background_pngs = glob.glob('bground*.png')
        background_jpgs = glob.glob('bground*.jpg')
        all_bgrounds = background_pngs + background_jpgs
        selected_bground = random.choice(all_bgrounds)
    elif background_img == "4":
        selected_bground = "bground04.png"
    elif background_img == "3":
        selected_bground = "bground03.jpg"
    elif background_img == "2":
        selected_bground = "bground02.jpg"
    elif background_img == "1":
        selected_bground = "bground01.png"
    
    os.chdir("src")
    os.chdir("characterA")
    if character_A == "5":
        characterA_pngs = glob.glob('characterA*.png')
        selected_charA = random.choice(characterA_pngs)
    elif character_A == "4":
        selected_charA = "characterA04.png"
    elif character_A == "3":
        selected_charA = "characterA03.jpg"
    elif character_A == "2":
        selected_charA = "characterA02.jpg"
    elif character_A == "1":
        selected_charA = "characterA01.png"

    os.chdir("src")    
    os.chdir("characterB")
    if character_B == "5":
        characterB_pngs = glob.glob('characterB*.png')
        selected_charB = random.choice(characterB_pngs)
    elif character_B == "4":
        selected_charB = "characterB04.png"
    elif character_B == "3":
        selected_charB = "characterB03.jpg"
    elif character_B == "2":
        selected_charB = "characterB02.jpg"
    elif character_B == "1":
        selected_charB = "characterB01.png"

    os.chdir("src")
    os.chdir("pet")
    if character_pet == "5":
        pet_pngs = glob.glob('pet*.png')
        selected_pet = random.choice(pet_pngs)
    elif character_pet == "4":
        selected_pet = "pet04.png"
    elif character_pet == "3":
        selected_pet = "pet03.jpg"
    elif character_pet == "2":
        selected_pet = "pet02.jpg"
    elif character_pet == "1":
        selected_pet = "pet01.png"
        
    if quote_select == "Y":
        with open("quotes_list.txt", 'r') as file:
            quotes = file.readlines()
            rand_quote = random.choice(quotes)



if __name__ == "__main__":
    main()