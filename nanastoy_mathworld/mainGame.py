import utils
import loot
import end
import random
import quiz
import time

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
    NoRewardDebuff = False
    utils.say("After you clicked the 'Yes' button on the website")
    utils.say("A very bright light appears on your screen")
    utils.say("And you can feel the exhaustion on your body like"
              " it's shutting down")
    utils.say("every black out...")
    utils.say("a while later, you started to feel yourself")
    utils.say("but...")
    utils.say("You just realized that something is weird")
    utils.say("You are not in your bedroom anymore")
    utils.say("Instead, you find yourself in the middle of the strange room")

    # some dialogue welcoming and explains the basic should be good here
    # gotcheatBreak = False
    # end3break = False

    while PlayerHP > 0:
        dx = utils.distance(PlayerPosX, PortalPosY)
        dy = utils.distance(PlayerPosY, PortalPosY)
        movesToWin = dx + dy - 1
        if movesToWin == 0:
            utils.say("You have reach the exit portal")
            utils.say("The strange shadow approaches you")
            utils.say("'I will not let you escape, human' said the shadow")
            utils.say("The shadow walks out of the dark spot")
            utils.say("The shadow appears to be Nanastoy")
            utils.say("'To exit this world, you must prove yourself to me!'")
            utils.say("'Prove yourself to me that you are smart enough'")
            utils.say("You feel like this will be challenging for you")
            utils.say("But you want to prove yourself to him")
            utils.say("THIS FILLED YOU WITH D E T E R M I N A T I O N")
            FinalAnswer = quiz.question("final")
            playerAnswer = float(input().strip())
            if playerAnswer == FinalAnswer:
                end.ending3()
                # end3break = True
                break
            else:
                utils.say("Incorrect Answer, the professor hits you and "
                          "he restarts this encounter once again...")
                PlayerHP -= 15
                time.sleep(3)
        elif ActionCount == ActionLimit:
            utils.say("Professor's right hand man has appeared in"
                      "front of you")
            utils.say("You have no choice but to fight him...")
            correctAnswer = quiz.question(difficulty)
            PlayerAns = float(input().strip())
            if PlayerAns == correctAnswer:
                utils.say("You hit the monster, hurting him, but it escaped"
                          " before you can get the final blow")
                utils.say("However, it left some stuff behind to collect!")
                PlayerHP += 10
                if PlayerHP > 45:
                    PlayerHP = 45
                if NoRewardDebuff is False:
                    rewards = loot.randomRewards()
                    Inventory[rewards] += 1
                NoRewardDebuff = False
                difficulty += 1
                if difficulty > 3:
                    difficulty = 3
            else:
                hitDamage = int(PlayerHP / 4)
                PlayerHP -= hitDamage
                utils.say(f"The gigantic monsters hit you for {hitDamage}")
                utils.say("then it escaped before you can strike back")
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
                    utils.say("The chest contains both good items and bad"
                              " items")
                    utils.say("It all depends on you")
                    utils.say("If you think you have good luck,"
                              " Take a chance.")
                    open = utils.choice("Do you open the chest?", "Yes", "No")
                    if open == "yes":
                        recievedItem = loot.randomAll()
                        if recievedItem in Inventory:
                            Inventory[recievedItem] += 1
                        elif recievedItem == "Cheating":
                            end.ending4()
                            break
                        elif recievedItem == "Increased Difficulty":
                            difficulty += 1
                            if difficulty > 3:
                                difficulty = 3
                        elif recievedItem == "Instant Damage":
                            instantDMG = random.randint(6, 10)
                            PlayerHP -= instantDMG
                        elif recievedItem == "No Reward Debuff":
                            NoRewardDebuff = True
                        ActionCount += 1
                    else:
                        utils.say("You decided not to open the chest")
                        utils.say("Guess you are not brave enough to open it")
                elif NewRoom == "monster":
                    utils.say("Oh no...there's something coming closer to you")
                    utils.say("You heard the sound of large footsteps")
                    utils.say("It's a huge scary looking monster appears in"
                              "front of you")
                    utils.say("Your legs are suddenly freeze")
                    utils.say("You can choose to fight or to dodge")
                    utils.say("If you choose to fight")
                    utils.say("the monster will give you some maths problem"
                              " to answer")
                    utils.say("If you answer wrong, the monster will"
                              " attack you")
                    utils.say("but if you answer it correctly")
                    utils.say("you will attack and defeat the monster"
                              " and minorly regenerates your health")
                    utils.say("If you choose to run away,")
                    utils.say("You will have a small chance of"
                              "successfully dodging and take no damage")
                    time.sleep(1)
                    action = utils.choice("Fight or Dodge?", "Fight", "Dodge")
                    if action == "fight":
                        correctAns = quiz.question(0)
                        playerAns = float(input().strip())
                        if playerAns == correctAns:
                            PlayerHP += 5
                            if PlayerHP > 45:
                                PlayerHP = 45
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
                    utils.say("You found some sort of a map in the room")
                    utils.say("Reading it should be useful to pinpoint your"
                              "location")
                    utils.say("However, It can take a long time to read it"
                              "as there are some pieces missing")
                    read = utils.choice("Do you read the map?", "Yes", "No")
                    if read == "yes":
                        utils.say(f"You require atleast {movesToWin} moves to"
                                  + "reach the portal")
                        ActionCount += 2
                    else:
                        utils.say("You decided not to look at it")
                        utils. say("You want it to be challenging, eh?")
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
                    confirmation = utils.choice("Are you sure though you"
                                                " want to use this?", "Yes",
                                                "No")
                    if confirmation == "yes":
                        Inventory[playerUse] -= 1
                        if playerUse == "Minor Heal":
                            randomHeal = random.randint(5, 10)
                            PlayerHP += randomHeal
                        elif playerUse == "Full Restore":
                            PlayerHP = 45
                        elif playerUse == "Reduce Difficulty":
                            difficulty -= 1
                            if difficulty < 1:
                                difficulty = 1
                        ActionCount += 1

    end.ending2()
