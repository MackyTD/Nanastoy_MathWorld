"""
This is a collection of a useful functions that would be used
repeatedly during the course of the game
"""
import time
import random
# import colorama


def say(text, color):
    time.sleep(1)
    print(text)
    # I will add color functionality later


def choice(prompt, *options):
    while True:
        say(prompt)
        for choice, option in enumerate(options):
            say(f"{choice + 1} : {option}")
        pChoice = str(input())
        for choice, option in enumerate(options):
            if pChoice == str(choice+1) or pChoice.lower() == option.lower():
                return option.lower()


def moving(posX, posY):
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


def randomLoot():
    allLoot = []
    RNG = random.randint(1, 200)
    if RNG == 1:
        receivedItem = allLoot[0]
    if 2 <= RNG <= 10:
        receivedItem = allLoot[1]
    # we can repeat this pattern for all the possible loot drop
    return receivedItem


def randomRewards():
    allLoot = []
    RNG = random.randint(1, 200)
    if RNG == 1:
        receivedItem = allLoot[0]
    if 2 <= RNG <= 10:
        receivedItem = allLoot[1]
    # we can repeat this pattern for all the GOOD loot drop
    return receivedItem


def countdown(sec):
    while True:
        time.sleep(1)
        sec -= 1
        if sec == 120:
            print("2 minutes remaining!")
        elif sec == 60:
            print("1 minutes remaining!")
        elif sec == 30:
            print("30 seconds remaining!")
        elif 0 < sec <= 10:
            print(sec)
        elif sec == 0:
            time.sleep(0.5)
            print("times up!")
            break
