from game_data import data
import random

def get_random_food():
    """Get data from random account"""
    return random.choice(data)

def format_data(food):
    """Format account into printable format: name, description and country"""
    name = food["name"]
    descriere = food["descriere"]
    calorii_count = food["calorii"]
    return f"{name},  {descriere} "


def check_answer(guess, a_calorii, b_calorii):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_calorii > b_calorii:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    game_should_continue = True
    food_a = get_random_food()
    food_b = get_random_food()

    while game_should_continue:
        food_a = food_b
        food_b = get_random_food()

        while food_a == food_b:
            food_b = get_random_food()

        print(f"Compare A: {format_data(food_a)}.")
        print(f"Against B: {format_data(food_b)}.")

        guess = input("Ce are mai multe calori? Type 'A' or 'B': ").lower()
        a_calorii_count = food_a["calorii"]
        b_calorii_count = food_b["calorii"]
        is_correct = check_answer(guess, a_calorii_count, b_calorii_count)


        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()