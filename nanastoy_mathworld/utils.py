"""
This is a collection of a useful functions that would be used
repeatedly during the course of the game
"""
import time
import random
from termcolor import colored

# this function will be used a lot in dialogue, Here's how to use it
# you can use only say("any text", "text color", "the bg color") and it
# will work, DONT use "say(colored())"


def say(text, color="white", bg=None):
    time.sleep(1)
    print(colored(text, color, bg))  # say function already defined with colors
# if you dont put any argument after the actual text, the default value will be
# used (normal white text), so you dont need to fill all 3 args eitherself.


def choice(prompt, *options):
    while True:
        say(prompt)
        for choice, option in enumerate(options):
            say(f"{choice + 1} : {option}")
        pChoice = str(input())
        for choice, option in enumerate(options):
            if pChoice == str(choice+1) or pChoice.lower() == option.lower():
                return option.lower()


def move(posX, posY):
    while True:
        moveOptions = []
        if posY != 7:
            moveOptions.append("Up")
        if posY != 1:
            moveOptions.append("Down")
        if posX != 1:
            moveOptions.append("Left")
        if posX != 7:
            moveOptions.append("Right")

        say("Which direction do you want to move?")
        for choice, direction in enumerate(moveOptions):
            say(f"{choice + 1} : {direction}")
        pMove = str(input())
        for choice, direction in enumerate(moveOptions):
            if pMove == str(choice+1) or pMove.lower() == direction.lower():
                return direction.lower()


def distance(Xa, Xb):
    return(abs(Xa-Xb))


def newRoom():
    allRooms = ["normal", "chest", "monster", "map"]
    randomRoom = allRooms[random.randint(0, 3)]
    return randomRoom
