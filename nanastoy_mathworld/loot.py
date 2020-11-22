import random
from utils import say
from termcolor import colored
import pyfiglet


def randomRewards():
    RNG = random.randint(1, 100)
    if 1 <= RNG <= 15:
        rewards = "Full Restore"
    elif 16 <= RNG <= 75:
        rewards = "Minor Healing"
    else:
        rewards = "Reduce Difficulty"
    say(colored(f"You found a {rewards} item in the chest!", "green"))
    say(colored("Seems like it is you lucky day today!", "yellow", "on_green"))
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
            no_rewards = pyfiglet.figlet_format("NO REWARDS", font="digital")
            say("WELL, you found ...")
            say(f"{no_rewards}", end='')
            say("HAHAHAHA, your bad luck")
            say("You just wasted your action")
        else:
            debuff = "None"
            say("You found literally nothing in the chest")
        return debuff


def description(item):
    if item == "Full Restore":
        say("description (what does it do?)", "green")
#  repeat for all items (in randomRewards)
