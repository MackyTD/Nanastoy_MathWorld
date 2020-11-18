# this file is the core gameplay loop/branch
import utils
import loot
import end
import random
import quiz
from time import sleep as wait


utils.say("backstory here, until before clicking the link")
response = utils.choice("Do you click the link in this website?", "Yes", "No")
if response == "no":
    end.ending1()
else:
    PlayerPosX = 4
    PlayerPosY = 4
    PlayerHP = 60
    ActionCount = 0
    ActionLimit = random.randint(5, 8)
    Inventory = []
    difficulty = 1
    Portal = ["1,1", "7,1", "1,7", "7,7"]
    spawnedPortal = Portal[random.randint(0, 3)]
    PortalPosX = int(spawnedPortal.split(",")[0])
    PortalPosY = int(spawnedPortal.split(",")[1])
    dx = utils.distance(PlayerPosX, PortalPosY)
    dy = utils.distance(PlayerPosY, PortalPosY)
    movesToWin = dx + dy
    utils.say("story")

while PlayerHP > 0:
    if movesToWin == 0:
        while True:
            FinalAnswer = quiz.question("final")
            playerAnswer = input()
            utils.say("You have 2.5 MINUTES to answer this question!")
            PlayerAns = input()
            timer = 150
            while len(PlayerAns) == 0:
                wait(1)
                timer -= 1
                if timer == 0:
                    PlayerAns == "not in time"
                    utils.say("Out of time!", "red")
                    break
            if playerAnswer == FinalAnswer:
                end.ending3()
                break
            else:
                PlayerHP -= 20
    elif ActionCount == ActionLimit:
        utils.say("placeholder")
        correctAnswer = quiz.question(difficulty)
        utils.say("You have 2 MINUTES to answer this question!")
        PlayerAns = input()
        timer = 120
        while len(PlayerAns) == 0:
            wait(1)
            timer -= 1
            if timer == 0:
                PlayerAns == "not in time"
                utils.say("Out of time!", "red")
                break
        if PlayerAns == correctAnswer:
            PlayerHP += 5
            if PlayerHP > 60:
                playerHP = 60
                difficulty += 1
                if difficulty > 3:
                    difficulty = 3
        else:
            hitDamage = int(PlayerHP / 4)
            PlayerHP -= hitDamage
            utils.say(f"The professor hit you for {hitDamage}")
            utils.say("then it escaped")
    else:
        response2 = utils.choice("What do you want to do?", "Move",
                                 "Use acquired items")
        if response2 == "move":
            direction = utils.move(PlayerPosX, PlayerPosY)
            if direction == "left":
                PlayerPosX -= 1
            elif direction == "right":
                PlayerPosX += 1
            elif direction == "up":
                PlayerPosY += 1
            else:
                PlayerPosY -= 1
            ActionCount += 1
            NewRoom = utils.newRoom()
            if NewRoom == "chest":
                utils.say("placeholder dialogue")
                action = utils.choice("Do you open the chest?", "Yes", "No")
                if action == "yes":
                    ActionCount += 1
                else:
                    utils.say("")
            elif NewRoom == "monster":
                utils.say("placeholder dialogue")
                action = utils.choice("Fight or Dodge?", "Fight", "Dodge")
                if action == "fight":
                    correctAns = quiz.question(0)
                    utils.say("You have 45 SECONDS to answer this question!")
                    PlayerAns = input()
                    timer = 45
                    while len(PlayerAns) == 0:
                        wait(1)
                        timer -= 1
                        if timer == 0:
                            PlayerAns == "not in time"
                            utils.say("Out of time!", "red")
                            break
                    if PlayerAns == correctAns:
                        PlayerHP += 5
                        if PlayerHP > 60:
                            playerHP = 60
                    else:
                        hitDamage = random.randint(4, 8)
                        PlayerHP -= hitDamage
                        utils.say(f"The monsters hit you for {hitDamage}")
                        utils.say("then it escaped")
                else:
                    a = random.randint(1, 3)
                    if a == 1:
                        utils.say("Dodge succeeded!", "green")
                    else:
                        utils.say("Dodge Failed!", "red")
                        hitDamage = random.randint(8, 10)
                        PlayerHP -= hitDamage
                        utils.say(f"The monsters hit you for {hitDamage}")
                        utils.say("then it escaped")
                    ActionCount += 1
            elif NewRoom == "map":
                utils.say("placeholder dialogue")
                action = utils.choice("Do you read the map?", "Yes", "No")
                if action == "yes":
                    utils.say(f"You require atleast {movesToWin} moves to"+"\n"
                              + "reach the portal")
                    ActionCount += 2
                else:
                    utils.say("placeholder dialogue")
        else:
            # Player choose use
            ActionCount += 1

end.ending2()
