import random
from utils import say
# you can create a whole new system for loot roll, I have no good way yet


def randomLoot(LootPool):
    items = []
    if LootPool == "all":
        items += []
    RNG = random.randint(1, 200)
    if RNG == 1:  # tweak this for varying percentages
        receivedItem = items[0]
    elif 2 <= RNG <= 10:
        receivedItem = items[1]
    else:
        receivedItem = "nothing"
    # we can repeat this pattern for all the possible loot drop
    say(f"You found {receivedItem} in the chest!", "green")
    return receivedItem


def description(item):
    if item == " ":
        say("what does the item do?", "green")
        # repeat for all usable items
