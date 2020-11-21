# say the question, then return the correct answer from the question
from utils import say
from random import randint, uniform


def question(difficulty):
    int_a, int_b, int_c = randint(1, 10)
    float_a, float_b, float_c = round(uniform(1, 10), 2)
    if difficulty == 0:  # very easy, 5 variations
        say("question")
        correctAnswer = "placeholder"
    elif difficulty == 1:  # 2 questions varients
        say("question")
        correctAnswer = "placeholder"
    elif difficulty == 2:  # 2 questions varients
        say("question")
        correctAnswer = "placeholder"
    elif difficulty == 3:  # 3 questions varients
        say("question")
        correctAnswer = "placeholder"
    elif difficulty == "final":  # some sort of BASIC calculus, 1 varient
        say("question")
        correctAnswer = "placeholder"
    return correctAnswer
