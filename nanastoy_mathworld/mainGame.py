# this file is the core gameplay loop/branch
import utils
import loot
import end
import random
import quiz
import pyfiglet

utils.say("You are studying for the upcoming calculus exam tomorrow")
utils.say("You are struggling with it so much")
utils.say("You decided to lookup for the practice problem on the internet")
utils.say("You spend a very long time looking for a good practice website")
utils.say("You found a mysterious website called 'Nanastoy's math world'")
utils.say("You thought to yourself 'This is kinda werid, should I visit this?'"
          )
LinkClick = utils.choice("Click the link to this website?", "Yes", "No")
if LinkClick == "no":
    end.ending1()
else:
    PlayerPosX = 4
    PlayerPosY = 4
    PlayerHP = 45
    ActionCount = 0
    ActionLimit = random.randint(5, 7)
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
    utils.say("----------------------"
              "     STORY PART 2     "
              "----------------------")

    # cheatBreak = False
    end3break = False

    while PlayerHP > 0:
        if movesToWin == 0:
            utils.say("placeholder")
            while True:
                FinalAnswer = quiz.question("final")
                playerAnswer = input().strip()
                if playerAnswer == FinalAnswer:
                    end.ending3()
                    end3break = True
                    break
                else:
                    PlayerHP -= 15
            if end3break:
                break
        elif ActionCount == ActionLimit:
            utils.say("placeholder")
            correctAnswer = quiz.question(difficulty)
            PlayerAns = input().strip()
            if PlayerAns == correctAnswer:
                PlayerHP += 10
                if PlayerHP > 45:
                    playerHP = 45
                if NoRewardDebuff is False:
                    rewards = loot.randomRewards()
                    Inventory[rewards] += 1
                NoRewardDebuff = False
                if difficulty < 3:
                    difficulty += 1
            else:
                hitDamage = int(PlayerHP / 4)
                PlayerHP -= hitDamage
                utils.say(f"The professor hit you for {hitDamage}")
                utils.say("then it escaped")
            ActionCount = 0
            ActionLimit = random.randint(5, 7)

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
                        elif recievedItem == "Cheating":
                            end.ending4()
                            break  # this SHOULD work, if not lmk
                        elif recievedItem == "Increased Difficulty":
                            if difficulty < 3:
                                difficulty += 1
                        elif recievedItem == "Instant Damage":
                            instantDMG = random.randint(5, 10)
                            playerHP -= instantDMG
                        elif recievedItem == "No Reward Debuff":
                            NoRewardDebuff = True
                        ActionCount += 1
                    else:
                        utils.say("placeholder")
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
                            hitDamage = random.randint(6, 8)
                            PlayerHP -= hitDamage
                            utils.say(f"The monsters hit you for {hitDamage}")
                            utils.say("then it escaped")
                    else:
                        a = random.randint(1, 3)
                        if a == 1:
                            utils.say("Dodge succeeded!", "green")
                        else:
                            utils.say("Dodge Failed!", "red")
                            monsHitDamage = random.randint(6, 9)
                            PlayerHP -= monsHitDamage
                            utils.say("The monsters hit you"
                                      f"for {monsHitDamage}")
                            utils.say("then it escaped")
                        ActionCount += 1
                elif NewRoom == "map":
                    utils.say("placeholder dialogue")
                    read = utils.choice("Do you read the map?", "Yes", "No")
                    if read == "yes":
                        utils.say(f"You require atleast {movesToWin} moves to"
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
                            playerUse = Item
                            useBreak = True
                            break
                    if useBreak:
                        break
                if playerUse in Inventory:
                    loot.description(playerUse)
                    confirmation = utils.choice("Are you sure?", "Yes", "No")
                    if confirmation == "yes":
                        Inventory[playerUse] -= 1
                        if playerUse == "Minor Heal":
                            randomHeal = random.randint(4, 8)
                            playerHP += randomHeal
                        elif playerUse == "Full Restore":
                            playerHP = 45
                            full_restore = pyfiglet.figlet_format("Congrats",
                                                                  font="epic")
                            utils.say("You have restored all your health"
                                      "points!!!")
                            utils.say(f"{full_restore}", end='')
                            utils.say("Now be cautious... ")
                            utils.say("You have gotten another life... "
                                      "Live it wisely")
                            utils.say("Stay focused and continue your journey"
                                      "...")
                        elif playerUse == "Reduce Difficulty":
                            if difficulty > 1:
                                difficulty -= 1
                            else:
                                utils.say("You are already at the lowest"
                                          "difficulty possible")
                                utils.say("But there will be no refunds of"
                                          "your item that you just used")
    # you can change the dialogue a bit
                        ActionCount += 1

    end.ending2()
