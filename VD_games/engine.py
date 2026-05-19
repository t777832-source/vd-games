import prompt


ROUNDS_COUNT = 3


def run_game(game_description, get_question_and_answer):
    print("Welcome to the VD-games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game_description)

    correct_answers = 0

    while correct_answers < ROUNDS_COUNT:
        question, correct_answer = get_question_and_answer()

        print(f"Question: {question}")

        answer = prompt.string("Your answer: ")

        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        print(f"Let's try again, {name}!")
        return

    print(f"Congratulations, {name}!")
