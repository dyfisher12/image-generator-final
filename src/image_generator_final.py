from PIL import Image, ImageFile
import random


def gather_inputs():
    background_img = input("Select your background: \nA) Death City \nB) Hyrule Field \nC) The Moon \nD) Minecraft Cave")
    character_A = input("Select your first character: \nA) Link \nB) Death the Kid \nC) Papa Emeritus IV \nD) Perry the Platypus")
    character_B = input("Select your second character: \nA) King Bob \nB) Geralt of Rivia \nC) Foxy \nD) Batman")
    character_pet = input("Select a pet for your characters: \nA) Garfield \nB) Navi \nC) Bolt \nD) Dimple")
    quote_select = input("Would you like to display a random generated quote? \nYes/No")

    