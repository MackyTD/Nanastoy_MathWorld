from utils import say
import pyfiglet


def ending1():  # didn't click the link
    say("some story here")


def ending2():  # lost all HP
    say("some story here")


def ending3():  # win
    say("some story here")


def ending4():  # got the instant lost item
    say("OH MY GOD ... WHAT A SHAME!!", "red")
    say("You have let your math professor down AND yourself")
    cheater = pyfiglet.figlet_format("CHEATER", font="poison")
    say("You are a")
    say(f"{cheater}")
    say("You have been caught doing this shameful act!")
    say("You have failed the challenge of Nanastoy Math World! "
        "Now you are stuck in this math world forever...")
