# say the question, then return the correct answer from the question
from utils import say
from random import randint, uniform


def question(difficulty):
    if difficulty == 0:  # add/minus
        varient_0 = randint(1, 5)
        if varient_0 == 1:
            varA = randint(14, 30)
            varB = round(uniform(15, 20), 2)
            say(f"Mary have {varA} little lambs and have the average weight"
                f" of {varB} kg")
            say("How many little lambs does Mary have in total?")
            correctAnswer = varA
        elif varient_0 == 2:
            varC, varD, varE = randint(12, 37)
            say(f"Jake have {varC} books at home. He went out and borrow"
                f" {varD} more books from the library." + "\n"
                f"He then buy {varE} more books from the shop")
            say("How many books does Jake have in total?")
            correctAnswer = varC + varD + varE
        elif varient_0 == 3:
            varF, varG = randint(12, 15)
            varH = randint(5, 10)
            say(f"A pizza shop prepared {varF} Pepperoni Pizza and {varG}"
                "Margherita Pizza." + "\n" + "Few customers enter and bought"
                f" a total of {varH} Pepperoni Pizzas")
            say("How many Pepporoni Pizza do this shop have left?")
            correctAnswer = varF - varH
        elif varient_0 == 4:
            varI, varJ = randint(130, 150)
            if varI < varJ:
                varJ += randint(30, 55)
            say("Bob has a big ant farm, and he decided to sell some of it"
                f"If he started with {varI} ants and sold {varH}")
            say("How many ants do he have left")
            correctAnswer = varI - varJ
        else:
            varK, varL = randint(150, 200)
            say(f"You sold a total of {varK} chocolate chips cookies and"
                f"{varL} vanilla cookie")
            say("How many cookie do you sold in total?")
            correctAnswer = varK + varL

    elif difficulty == 1:  # 3 questions varients
        varient_1 = randint(1, 3)
        if varient_1 == 1:
            pass
        elif varient_1 == 2:
            pass
        else:
            pass
    elif difficulty == 2:  # 3 questions varients
        varient_2 = randint(1, 3)
        if varient_2 == 1:
            pass
        elif varient_2 == 2:
            pass
        else:
            pass
    elif difficulty == 3:  # 4 questions varients
        varient_3 = randint(1, 4)
        if varient_3 == 1:
            pass
        elif varient_3 == 2:
            pass
        else:
            pass
    elif difficulty == "final":  # some sort of BASIC calculus, 2 varient
        varient_f = randint(1, 2)
        if varient_f == 1:
            pass
        else:
            pass
    return correctAnswer
