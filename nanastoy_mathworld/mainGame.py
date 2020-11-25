# this file is the core gameplay loop/branch
import utils
import loot
import end
import random
import quiz

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
    utils.say("After you clicked the 'Yes' button on the website")
          say("A very bright light appears on your screen")
          say("And you can feel the exhaustion on your body like it's shutting down")
          say("every black out...")
          say("a while later, you started to feel yourself")
          say("but...")
          say("You just realized that something is weird")
          say("You are not in your bedroom anymore")
          say("but in the middle of the strange room")

    # cheatBreak = False
    end3break = False

    while PlayerHP > 0:
        if movesToWin == 0:
            utils.say("You have reach the exit portal")
                  say("The strange shadow approaches you")
                  say("'I will not let you escape, human' said the shadow")
                  say("The shadow walks out of the dark spot")
                  say("The shadow appears to be Nanastoy")
                  say("'To exit this world, you must prove yourself to me!'")
                  say("'Prove yourself to me that you are smart enough'")
                  say("You feel like this will be challenging for you")
                  say("But you want to prove yourself to him")
                  say("THIS FILLED YOU WITH D E T E R M I N A T I O N")
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
            utils.say("You have reached you moves limit")
                  say("You will be forced to take on the math monster")
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
                    utils.say("Oh look! you found a chest")
                say("The chest contains both good items and bad items")
                say("It all depends on you")
                say("If you think you have good luck. Take a chance.")
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
                        utils.say("You decided not to open the chest")
                              say("Guess you are not brave enough to open it")
                elif NewRoom == "monster":
                utils.say("Oh no...there's something coming closer to you")
            say("You heard the sound of large footsteps")
            say("It's a huge scary looking monster appears in front of you")
            say("Your legs are suddenly freeze")
            say("You can choose to fight or to dodge")
            say("If you choose to fight")
            say("the monster will give you some maths problem to answer")
            say("If you answer wrong, the monster will attack you")
            say("but if you answer it correctly")
            say("you can attack and defeat the monster ะน gain experiences")
            say("Or if you choose to run away")
            say("You will have very less chance to dodge successfully")
            say("You won't get any damage from the monster")
            say("If your dodge is not successful")
            say("You will be hit by the monster and lose random amount of HP")
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
                    utils.say("This is the map to the exit portal")
                          say("After you read the map")
                          say("It will tell you how many moves to reach the portal")
                    read = utils.choice("Do you read the map?", "Yes", "No")
                    if read == "yes":
                        utils.say(f"You require atleast {movesToWin} moves to"
                                  + "reach the portal")
                        ActionCount += 2
                    else:
                        utils.say("You decided not to look at it")
                              say("You want it to be challenging, eh?")
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
