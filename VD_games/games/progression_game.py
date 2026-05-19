import random


DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        progression.append(start + index * step)

    return progression


def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = 10

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)

    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, str(correct_answer)
