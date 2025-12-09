from PIL import Image, ImageFile
import random
import glob
import os

def main():

    
    background_img = input("Select your background: \n1) Death City \n2) Hyrule Field \n3) The Moon \n4) Minecraft Cave \n5) Random")
    character_A = input("Select your first character: \n1) Link \n2) Death the Kid \n3) Papa Emeritus II \n4) Perry the Platypus \n5) Random")
    character_B = input("Select your second character: \n1) King Bob \n2) Geralt of Rivia \n3) Foxy \n4) Batman \n5) Random")
    character_pet = input("Select a pet for your characters: \n1) Garfield \n2) Navi \n3) Bolt \n4) Dimple \n5) Random")
    quote_select = input("Would you like to display a randomly generated quote? \nYes/No")

    def create_image():
        if background_img == "5":
            background_pngs = glob.glob('bground*.png')
            background_jpgs = glob.glob('bground*.jpg')
            all_bgrounds = background_pngs + background_jpgs
            selected_img = random.choice(all_bgrounds)
        elif background_img == "4":
            selected_img = bground


        
    
    create_image()