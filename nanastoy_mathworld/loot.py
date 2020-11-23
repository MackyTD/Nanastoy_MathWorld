import random
from utils import say
import pyfiglet


def randomRewards():
    RNG = random.randint(1, 50)
    if 1 <= RNG <= 5:
        rewards = "Full Restore"
    elif 6 <= RNG <= 40:
        rewards = "Minor Heal"
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
        if 2 <= RNG <= 35:
            debuff = "Instant Damage"
            say("You just stepped on the path of self-harm!")
            say("Don't get what I am saying?... "
                "Well you YOURSELF caused your health points to decrease")
            say("You recieved instantaneous damage from this unpredictable"
                "loot box")
            say("Now pray that your health points don't get too low or else..."
                )
        if 36 <= RNG <= 50:
            debuff = "Increase Difficulty"
            say("Ooops", "red")
            say("I feel extremely sorry for you...")
            say("I hope you are a good mathematician or atleast have good"
                "COMMON SENSE")
            say("If not, prepare yourself to face a nightmarishly difficult"
                "question in your next encounter with the math monster or"
                "the professor")
            say("Because your reward is to get a harder question next time")
            say("Hahaha, don't worry you've got this")
        if 51 <= RNG <= 65:
            debuff = "No Rewards Debuff"
            # This is the item that makes the next time that you should've
            # got something from the professor (answer correctly)
            # The player would get no rewards
        else:
            debuff = "Nothing"
            no_rewards = pyfiglet.figlet_format("NOTHING", font="digital")
            say("WELL, you found ...")
            say(f"{no_rewards}", end='')
            say("HAHAHAHA, your bad luck")
            say("You just wasted your action")
        return debuff


def description(item):
    if item == "Full Restore":
        say("description (what does it do?)", "green")
    if item == "Minor Heal":
        say("description", "green")
    if item == "Reduce Difficulty":
        say("discription", "green")
