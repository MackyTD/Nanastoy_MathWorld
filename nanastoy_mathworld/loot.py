import random
from utils import say
import pyfiglet
# There is no need to add colored after say :
# ex. don't use say(colored('text'))
# read more about say at utils.py


def randomRewards():
    RNG = random.randint(1, 100)
    if 1 <= RNG <= 15:
        rewards = "Full Restore"
    elif 16 <= RNG <= 75:
        rewards = "Minor Healing"
    else:
        rewards = "Reduce Difficulty"
    say(f"You found a {rewards} item in the chest!", "green")
    say("Seems like it is your lucky day today!", "yellow", "on_green")
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
            say("OH MY GOD ... WHAT A SHAME!!", "red")
            say("You have let your math professor down AND yourself")
            cheater = pyfiglet.figlet_format("CHEATER", font="poison")
            say("You are a")
            say(f"{cheater}")
            say("You have been caught doing this shameful act!")
            say("You have failed the challenge of Nanastoy Math World! "
                "Now you are stuck in this math world forever")
        if 2 <= RNG <= 35:
            debuff = "Instant Damage"
            say("dialogue")
        if 36 <= RNG <= 50:
            debuff = "Increase Difficulty"
            say("dialogue")
        if 51 <= RNG <= 65:
            debuff = "No Rewards"
            # This is the item that makes the next time that you should've
            # got something from the professor (answer correctly)
            # The player would get no rewards
        else:
            debuff = "Nothing"
            no_rewards = pyfiglet.figlet_format("NO REWARDS", font="digital")
            say("WELL, you found ...")
            say(f"{no_rewards}", end='')
            say("HAHAHAHA, your bad luck")
            say("You just wasted your action")
        return debuff


def description(item):
    if item == "Full Restore":
        say("description (what does it do?)", "green")
#  repeat for all items (in randomRewards)
