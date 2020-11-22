# this file is the core gameplay loop/branch
import utils
import loot
import end
import random
import quiz

utils.say("backstory here, until before clicking the link")
LinkClick = utils.choice("Do you click the link in this website?", "Yes", "No")
if LinkClick == "no":
    end.ending1()
else:
    PlayerPosX = 4
    PlayerPosY = 4
    PlayerHP = 60
    ActionCount = 0
    ActionLimit = random.randint(4, 6)
    Inventory = {
        "Minor Heal": 0,
        "Full Restore": 0,
        "Reduce Difficulty": 0,
    }
    difficulty = 1
    Portal = ["1,1", "7,1", "1,7", "7,7"]
    spawnedPortal = Portal[random.randint(0, 3)]
    PortalPosX = int(spawnedPortal.split(",")[0])
    PortalPosY = int(spawnedPortal.split(",")[1])
    dx = utils.distance(PlayerPosX, PortalPosY)
    dy = utils.distance(PlayerPosY, PortalPosY)
    movesToWin = dx + dy
    NoRewardDebuff = False
    utils.say("story part 2")

cheatBreak = False
break2 = False

while PlayerHP > 0:
    if movesToWin == 0:
        utils.say("placeholder")
        while True:
            FinalAnswer = quiz.question("final")
            playerAnswer = input().strip()
            if playerAnswer == FinalAnswer:
                end.ending3()
                break2 = True
                break
            else:
                PlayerHP -= 20
        if break2:
            break
    elif ActionCount == ActionLimit:
        utils.say("placeholder")
        correctAnswer = quiz.question(difficulty)
        PlayerAns = input().strip()
        if PlayerAns == correctAnswer:
            PlayerHP += 10
            #  check for no reward debuff - active or not?
            rewards = loot.randomRewards()
            Inventory[rewards] += 1
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
        NormalAction = utils.choice("What do you want to do?", "Move",
                                    "Use acquired items")
        if NormalAction == "move":
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
                open = utils.choice("Do you open the chest?", "Yes", "No")
                if open == "yes":
                    recievedItem = loot.randomAll()
                    if recievedItem in Inventory:
                        Inventory[recievedItem] += 1
                    else:
                        pass  # add effects for debuff here
                    ActionCount += 1
                else:
                    utils.say("")
            elif NewRoom == "monster":
                utils.say("placeholder dialogue")
                action = utils.choice("Fight or Dodge?", "Fight", "Dodge")
                if action == "fight":
                    correctAns = quiz.question(0)
                    playerAns = input().strip()
                    if playerAns == correctAns:
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
                read = utils.choice("Do you read the map?", "Yes", "No")
                if read == "yes":
                    utils.say(f"You require atleast {movesToWin} moves to"+"\n"
                              + "reach the portal")
                    ActionCount += 2
                else:
                    utils.say("placeholder dialogue")
        else:
            while True:
                utils.say("What item do you want to use?")
                itemChoice = []
                for item in Inventory:
                    if Inventory[item] != 0:
                        itemChoice.append(item)
                itemChoice.append("Cancel")
                for numChoice, Item in enumerate(itemChoice):
                    utils.say(f"{numChoice + 1} : {Item}")
                playerUse = input().strip()
                for numChoice, Item in enumerate(itemChoice):
                    if playerUse == str(numChoice+1) or \
                       playerUse.lower() == Item.lower():
                        playerUse = Item.lower()
                        break
            if playerUse in Inventory:
                loot.description(playerUse)
                confirmation = utils.choice("Are you sure?", "Yes", "No")
                if confirmation == "yes":
                    Inventory[playerUse] -= 1
                    if playerUse == "item":
                        "do something"
                    elif playerUse == "another item":
                        pass
                    elif playerUse == "last item":
                        pass
# add action for all usable items : minor HP, Full Restore and reduce current difficulty
                    ActionCount += 1

end.ending2()
