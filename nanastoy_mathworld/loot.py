import random
from utils import say
# you can create a whole new system for loot roll, I have no good way yet


def randomRewards():
    RNG = random.randint(1, 100)
    if 1 <= RNG <= 10:
        rewards = "Full Restore"
    elif 11 <= RNG <= 60:
        rewards = "Minor Healing"
    elif 61 <= RNG <= 80:
        rewards = "Reduce Difficulty"
    else:
        rewards = "Hints"
    say(f"You found a {rewards} item in the chest!", "green")
    return rewards


def randomAll():
    LuckTest = random.randint(1, 2)
    if LuckTest == 1:
        recievedItem = randomRewards()
        return recievedItem
    else:
        RNG = random.randint(1, 100)
        if RNG == 1:
            debuff = "Cheating"
        if 2 <= RNG <= 35:
            debuff = "Instant Damage"
        if 36 <= RNG <= 50:
            debuff = "Increase Difficulty"
        if 51 <= RNG <= 65:
            debuff = "No Rewards"
        else:
            debuff = "None"
            say("You found literally nothing in the chest")
        return debuff


def description(item):
    if item == " ":
        say("what does the item do?", "green")
        # repeat for all usable items
