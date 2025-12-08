from PIL import Image, ImageFile
import random


def gather_inputs():
    background_img = input("Select your background: \nDeath City \nHyrule Field \nThe Moon \nMinecraft Cave")
    character_A = input("Select your first character: \nLink \nDeath the Kid \nPapa Emeritus IV \n Perry the Platypus")
    character_B = input("Select your second character: \nKing Bob \nGeralt of Rivia \nFoxy \nBatman")
    character_pet = input("Select a pet for your characters: \nGarfield \nNavi \nBolt \nDimple")
    quote_select = input("Would you like to display a random generated quote? \nYes/No")

    