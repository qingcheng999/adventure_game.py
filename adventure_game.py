import time
import random
import string
players = ["dragon", "pirate", "zombie", "wicked fairie", "troll"]
enemy = random.choice(players)


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(0.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=0):
    typewriter_simulator(message)
    time.sleep(delay)


def valid_input(prompt,  options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'The option "{option}" is invalid. Please try again.')


def intro(enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wild flowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere"
                " around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dragger.\n")


def field(weapon, enemy):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?\n", 1)
    response = valid_input("(Please enter 1 or 2.)\n", ['1', '2'])
    if response == '1':
        house(weapon, enemy)
    else:
        cave(weapon, enemy)


def house(weapon, enemy):
    print_pause("You approach the door of the house.", 1)
    print_pause("You are about to knock when the door opens"
                f" and out steps a {enemy}.", 1)
    print_pause(f"Eep! This is the {enemy}'s house!", 1)
    print_pause(f"The {enemy} attacks you!", 1)
    if 'Sword' not in weapon:
        print_pause("You feel a bit under-prepareed for this, "
                    "what with only having a tiny dagger.", 1)
    response = valid_input("Would you like to (1) fight or (2) run away?",
                           ['1', '2'])
    if response == '1':
        fight(weapon, enemy)
    else:
        print_pause("You run back into the field. Luckily, you don't"
                    " seem to have been followed.")
        field(weapon, enemy)


def cave(weapon, enemy):
    print_pause("You peer cautionsly into the cave.", 1)
    if "Sword" in weapon:
        print_pause("You've been here before, and gotten all the good"
                    " stuff. It's just an empty cave now. You walk"
                    " backout to the field.", 1)
    else:
        print_pause("It turns out to be only a very small cave.", 1)
        print_pause("Your eye catches a glint of metal behind a rock.", 1)
        print_pause("You have found the magical Sword of Ogoroth!", 1)
        print_pause("You discard your silly odd agger and take the "
                    "sword with you.", 1)
        print_pause("You walk back out to the field.", 1)
        weapon.append("Sword")
    field(weapon, enemy)


def fight(weapon, enemy):
    if "Sword" in weapon:
        print_pause(f"As the {enemy} moves to attack, you unsheath"
                    " your new sword.", 1)
        print_pause("The Sword of Ogoroth shines brightly in our "
                    "hand as you brace yourself for the attack.", 1)
        print_pause(f"But the {enemy} takes one look at your shiny"
                    " new toy and runs away!", 1)
        print_pause(f"You have rid the town of the {enemy}. You"
                    " are victorious!", 1)
    else:
        print_pause("You do your best...", 1)
        print_pause(f"But your dagger is no match for the {enemy}.", 1)
        print_pause("You have been defeated!", 1)


def play_again():
    response = valid_input("Would you like to play again? (y/n)", ['y', 'n'])
    if response == 'y':
        print_pause("Excellent! Restarting the game ...")
        global enemy
        enemy = random.choice(players)
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")
        exit(0)


def play_game():
    weapon = []
    intro(enemy)
    field(weapon, enemy)
    play_again()


if __name__ == '__main__':
    play_game()
