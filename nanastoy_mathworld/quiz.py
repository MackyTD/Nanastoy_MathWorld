from utils import say
from random import randint, uniform
import math


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
            varC = randint(10, 26)
            varD = randint(22, 35)
            varE = randint(12, 37)
            say(f"Jake have {varC} books at home. He went out and borrow"
                f" {varD} more books from the library." + "\n"
                f"He then buy {varE} more books from the shop")
            say("How many books does Jake have in total?")
            correctAnswer = varC + varD + varE
        elif varient_0 == 3:
            varF = randint(13, 20)
            varG = randint(9, 17)
            varH = randint(5, 10)
            say(f"A pizza shop prepared {varF} Pepperoni Pizza and {varG}"
                "Margherita Pizza." + "\n" + "Few customers enter and bought"
                f" a total of {varH} Pepperoni Pizzas")
            say("How many Pepporoni Pizza do this shop have left?")
            correctAnswer = varF - varH
        elif varient_0 == 4:
            varI = randint(180, 230)
            varJ = randint(120, 175)
            say("Bob has a big ant farm, and he decided to sell some of it"
                f"If he started with {varI} ants and sold {varJ}")
            say("How many ants do he have left")
            correctAnswer = varI - varJ
        else:
            varK = randint(120, 200)
            varL = randint(150, 200)
            say(f"You sold a total of {varK} chocolate chips cookies and"
                f"{varL} vanilla cookie")
            say("How many cookie do you sold in total?")
            correctAnswer = varK + varL

    elif difficulty == 1:  # basic multiply/division
        varient_1 = randint(1, 3)
        if varient_1 == 1:
            VarA = randint(4, 8)
            VarB = randint(42, 60)
            say(f"Jerome purchased {VarA} bags of candy, each one have {VarB}"
                " pieces of candy")
            say("How many pieces of candy does Jerome has?")
            correctAnswer = VarA * VarB
        elif varient_1 == 2:
            VarC = randint(3, 7)
            VarD = round(uniform(6, 8), 2)
            say(f"Thomas bought {VarC} dozen of donuts, each box costs"
                f"{VarD} dollars")
            say("How much donuts does Thomas have?")
            correctAnswer = 12 * VarC
        else:
            VarE = randint(20, 30)
            VarF = randint(12, 25) * VarE
            say(f"There's a total of {VarF} candies, and there are {VarE}"
                " student in the class")
            say("If the candy is split evenly to all students, how much candy"
                " will each of the student get?")
            correctAnswer = VarF / VarE

    elif difficulty == 2:  # decimals / division with some roundings
        varient_2 = randint(1, 3)
        if varient_2 == 1:
            VarG = randint(400, 600)
            VarH = randint(30, 40)
            say(f"There are {VarG} people waiting to board the SpaceX"
                f" Sentinal-6, which can contain {VarH} amount of people")
            say("What is the minimum roundtrips does the Sentinal-6 need"
                " to be enough for all the people")
            correctAnswer = math.ceil(VarG / VarH)
        elif varient_2 == 2:
            VarI = round(uniform(2, 9), 1)
            say(f"If an unknown beverage has a total of {VarI} grams of sugar")
            say("How many can of this drinks can Peter take before"
                " getting over 100 grams of sugar limit that he set?")
            correctAnswer = math.floor(100 / VarI)
        else:
            VarJ = randint(3, 6)
            VarK = round(uniform(5, 8), 2)
            say(f" A burger costs {VarK} dollars a piece. Sam and his friends"
                f" bought a total of {VarJ} pieces in total")
            say("How much did it cost them?")
            correctAnswer = VarJ * VarK

    elif difficulty == 3:
        varient_3 = randint(1, 3)
        if varient_3 == 1:
            var_a = round(uniform(1, 10), 1)
            var_b = round(uniform(3, 8), 2)
            say(f"What is the slope of a line that pass through the origin"
                f" and the point {var_a}, {var_b}?")
            correctAnswer = var_b / var_a
        elif varient_3 == 2:
            var_c = randint(30, 40)
            var_d = var_c + 1
            say("Two positive, consecutive integers have a product of "
                f"{var_c*var_d}")
            say("what is the the sum of both integers?")
            correctAnswer = var_c + var_d
        else:
            var_e, var_f = randint(-8, 8)
            say("What is the sum of all the coefficients of the quadratic"
                f" equation that have {var_e} and {var_f} as answers?")
            correctAnswer = (var_e * var_f) - var_e - var_f + 1
    elif difficulty == "final":
        varient_f = randint(1, 2)
        if varient_f == 1:
            Var_A = round(uniform(3, 8), 2)
            say(f"The radius of a circle is incresing at the rate of {Var_A}"
                " cm/s.")
            say("What is the rate of which the circumference increases?"
                "(answer in a multiple of pi)")
            correctAnswer = 2*Var_A
        else:
            A = randint(1, 5)
            B = randint(-3, 7)
            C = randint(-8, 17)
            x = randint(0, 6)
            say(f"Given f(x) is equal to {A}x^2 + {B}x + {C}")
            say(f"What is the slope at x = {x}")
            correctAnswer = 2*A*x + B
    return float(correctAnswer)
