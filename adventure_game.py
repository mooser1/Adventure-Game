import time
import random


def print_sleep(message, wait_time):
    print(message)
    time.sleep(wait_time)


def combat(payload, items, planets_visited, planet):
    space_objects = ['pirate', 'space worm', 'asteroid',
                     'imperial fighter', 'rebel fighter']
    space_object = ''
    space_object = random.choice(space_objects)
    print_sleep(f"Out of nowhere a {space_object} confronts you!!!", 2)
    if space_object == "pirate" or space_object == "space worm":
        if payload == "mining laser":
            print_sleep(f"A {payload} is known to be weak against "
                        "anything other than rock...", 2)
        elif payload == "mega laser":
            print_sleep(f"A {payload} is known to be "
                        "blast anything apart...", 2)
        choice = input("Would you like to (1) fight or (2) fly away?\n")
        if choice == '1':
            if payload == "mining laser":
                print_sleep(f"You do your best...", 1)
                print_sleep(f"but your {payload} is no match "
                            "for the {space_object}.", 2)
                print_sleep(f"You have been defeated!""", 2)
            elif payload == "mega laser":
                print_sleep(f"As the {space_object} moves to attack, "
                            "you fire your laser directly at it.", 2)
                print_sleep(f"The {space_object} explodes into pieces.", 2)
                print_sleep(f"With the {space_object} out of the way. "
                            "You make your way to the planet.", 3)
        elif choice == '2':
            print_sleep(f"You head back to the space port. "
                        "Luckily you managed to outrun the {space_object}.", 2)
            where_to(payload, items, planets_visited, planet)
    elif space_object == "imperial fighter" or space_object == "rebel fighter":
        print_sleep(f"I wouldnt mess with these guys, "
                    "they have heavy firepower!", 2)
    elif space_object == "asteroid":
        print_sleep(f"You use your {payload} to blast away the asteroid", 1)
        print_sleep("and continue you're journey to the planet", 1)


def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n")
        if choice == 'n':
            print_sleep("Thanks for playing! See you next time.", 2)
            return 'game_over'
        elif choice == 'y':
            print_sleep("Excellent! Restarting the game ...", 2)
            return 'running'


def intro():
    print_sleep("You're waiting in your ship at spaceport.", 1)
    print_sleep("There are 3 local planets to visit", 1)
    print_sleep("But there is known to be enemies out there", 1)
    print_sleep("in the depths of space", 1)
    print_sleep("All you have on the ship, is your mining laser", 1)
    print_sleep("Who knows what you will find....", 1)


def where_to(payload, items, planets_visited, planet):
    print_sleep("", 1)
    print_sleep("The blue planet is a water planet", 1)
    print_sleep("The yellow planet is a desert planet", 1)
    print_sleep("There is also a red planet that is "
                "home to the imperial city", 1)
    print_sleep("Please tell the stardrive which color", 0)
    print_sleep("planet you would like to visit?", 0)
    planet = ''
    while planet not in ['blue', 'yellow', 'red']:
        planet = input("Blue, Yellow or Red Planet?\n")
        if planet in planets_visited:
            print_sleep("You have already been here...", 1)
    space_travel(payload, items, planets_visited, planet)
    if planet.lower() == "blue":
        blue_planet(payload, items, planets_visited, planet)
    elif planet.lower() == 'yellow':
        yellow_planet(payload, items, planets_visited, planet)
    elif planet.lower() == 'red':
        red_planet(payload, items, planets_visited, planet)


def space_travel(payload, items, planets_visited, planet):
    print_sleep(f"You program the star drive to "
                "head to the {planet} planet", 1)
    print_sleep("After a few moments, you find "
                "yourself in space.", 1)
    combat(payload, items, planets_visited, planet)


def blue_planet(payload, items, planets_visited, planet):
    print_sleep(f"You arrive at the {planet} planet "
                "and find a small docking port", 1)
    if "imperial pass" in items:
        print_sleep("The port guard greets you, but she has already "
                    "issued your imperial pass, so there is nothing "
                    "more to do here now.", 1)
    else:
        print_sleep("The port administrator greets you "
                    "and gives you your ID "
                    "card.", 1)
        items.append("imperial pass")
    print_sleep("You head back to the ship.", 1)
    planets_visited.append("blue")
    where_to(payload, items, planets_visited, planet)


def yellow_planet(payload, items, planets_visited, planet):
    print_sleep("You arrive at the yellow desert planet "
                "and find a large space port", 1)
    if "imperial pass 2" in items:
        print_sleep("The port guard greets you, but she has already "
                    "issued your imperial pass, so there is nothing "
                    "more to do here now.", 1)
    else:
        print_sleep("The port administrator greets you "
                    "and gives you your ID "
                    "card.", 1)
        items.append("imperial pass 2")
    if payload == "mining laser":
        payload = "mega laser"
        print_sleep(f"You found a {payload} in some wreckage "
                    "in the desert!!!", 1)
    else:
        print_sleep("You rummage through some wreckage, "
                    "but nothing of interest is found.", 1)
    print_sleep("You head back to the ship.", 1)
    planets_visited.append("yellow")
    where_to(payload, items, planets_visited, planet)


def red_planet(payload, items, planets_visited, planet):
    print_sleep("You arrive at the red planet and find "
                "the Imperial Kingdom", 1)
    if "imperial pass" in items and "imperial pass 2" in items:
        print_sleep("The Emperor is waiting your presence. "
                    "You are to be a new sith Lord", 1)
    else:
        print_sleep("No one cares you are here yet", 1)
        print_sleep("You head back to the ship.", 1)
        where_to(payload, items, planets_visited, planet)
    planets_visited.append("red")


def play_game():
    game_state = 'running'
    while game_state == 'running':
        payload = "mining laser"
        items = []
        planets_visited = []
        game_state = 'running'
        planet = ''
        intro()
        where_to(payload, items, planets_visited, planet)
        game_state = play_again()


play_game()
