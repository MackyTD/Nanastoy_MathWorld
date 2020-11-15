"""
The creation of random room when player moves into a new spot
"""
import random
from utils import say


def newRoom():
    allRooms = ["normal", "chest", "monster", "map"]
    randomRoom = allRooms[random.randint(0, 3)]
    if randomRoom == "chest":
        say("placeholder dialogue")
    elif randomRoom == "monster":
        say("placeholder dialogue")
    elif randomRoom == "map":
        say("placeholder dialogue")
    else:
        say("placeholder dialogue")
