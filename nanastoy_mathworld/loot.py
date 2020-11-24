import random
from utils import say
import pyfiglet
import time


def randomRewards():
    RNG = random.randint(1, 50)
    if 1 <= RNG <= 5:
        rewards = "Full Restore"
    elif 6 <= RNG <= 32:
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
        elif 2 <= RNG <= 35:
            debuff = "Instant Damage"
            say("You just stepped on the path of self-harm!", "red")
            say("Don't get what I am saying?... "
                "Well you YOURSELF caused your health points to decrease")
            say("You recieved instantaneous damage from this unpredictable"
                " loot box")
            say("Now pray that your health points don't get too low"
                "or else...", "red")
        elif 36 <= RNG <= 50:
            debuff = "Increase Difficulty"
            say("Ooops", "red")
            say("I feel extremely sorry for you...")
            say("I hope you are a good mathematician or atleast have good"
                "COMMON SENSE")
            say("If not, prepare yourself to face a nightmarishly difficult"
                "question in your next encounter with the professor")
            say("Because your reward is to get a harder question next time")
            say("Hahaha, don't worry you've got this")
        elif 51 <= RNG <= 65:
            debuff = "No Rewards Debuff"
            say("Ohh no!!")
            say("What can be worst than not getting a reward for your"
                " hard work", "red")
            say("Confused??")
            say("Well you just obtained the item that is going to stop you"
                "from getting the good rewards from the lootbox even if you"
                " answer the math question correctly next time and make the"
                " math professor happy")
            say("I feel really bad for you ... 😞")
        else:
            debuff = "Nothing"
            no_rewards = pyfiglet.figlet_format("NOTHING", font="digital")
            say("WELL, you found ...")
            time.sleep(1)
            print(f"{no_rewards}", end='')
            say("HAHAHAHA, your bad luck")
            say("You just wasted your action")
        return debuff


def description(item):
    if item == "Full Restore":
        say("Before you use this do you know what this power does?")
        say("Well let me tell you...")
        say("Do you want to suddenly feel super energetic?", "blue")
        say("Do you want to conquer this whole math world?", "blue")
        say("Did you not realise this ultimate power was with you ever since?")
        say("The FULL RESTORE power, which will restore all your health"
            "points", "green")
        say("All your pain and suffering will be gone and you will feel like"
            "you have taken a rebirth in this math world")
        say("Wondering why you haven't used this power yet?")
        say("Well its not too late...")
    if item == "Minor Heal":
        say("Ohh, so you are already tired")
        say("Seems like this math world is killing you")
        say("Well, don't worry kid you have the Minor heal"
            "This will help restore some of your health points 🔋", "green")
    if item == "Reduce Difficulty":
        say("Ohh, seems like math is not your cup of tea")
        say("That's why you wanna use the Reduce difficulty item ..."
            "You think this will solve everything, right?")
        say("Well not everything BUT it will definitely help you"
            "to get a easier question in your next encounter with the"
            "professor", "green")
