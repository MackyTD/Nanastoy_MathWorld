import random
from utils import say


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
            say("dialogue")
        if 2 <= RNG <= 35:
            debuff = "Instant Damage"
            say("dialogue")
        if 36 <= RNG <= 50:
            debuff = "Increase Difficulty"
            say("dialogue")
        if 51 <= RNG <= 65:
            debuff = "No Rewards"
            say("dialogue")
        else:
            debuff = "None"
            say("You found literally nothing in the chest")
        return debuff


def description(item):
    if item == "Full Restore":
        say("description (what does it do?)", "green")
#  repeat for all items (in randomRewards)
