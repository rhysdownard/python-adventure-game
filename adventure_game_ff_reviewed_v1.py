import time
import random


def print_pause(message_pause):
    print(message_pause)
    time.sleep(2)


items = []
# options = ["red", "1", "2", "3", "attack", "run"]

doors = ["red", "green", "yellow"]
numbers = ["1", "2", "3"]
choices = ["yes", "no"]
fight_choices = ["attack", "run"]


def valid_choices(prompt, choices):
    while True:
        response = input(prompt).lower()
        for choice in choices:
            if choice == response:
                return response
        print_pause("Sorry, I don\'t understand.")


def valid_input_convo(prompt, numbers):
    # numbers = ["1","2","3"]
    while True:
        response = input(prompt).lower()
        for number in numbers:
            if number in response:
                return response
        print_pause("Sorry, I don\'t understand.")


def valid_input_door(prompt, doors):
    # doors = ["red", "green", "yellow"]
    while True:
        response = input(prompt).lower()
        for door in doors:
            if door in response:
                return response
        print_pause("Sorry, I don\'t understand.")


def valid_fight_choices(prompt, choices):
    # fight_choices = ["attack","run"]
    while True:
        response = input(prompt).lower()
        for fight_choice in fight_choices:
            if fight_choice in response:
                return response
        print_pause("Sorry, I don\'t understand.")


def intro():
    print_pause("It is dark and clammy as you open your eyes")
    print_pause("you find yourelf in a dark dungeon")
    print_pause("You are uninjured and inspect your belongings")
    print_pause("You have a small knife and a bronze key you don't recognise")
    print_pause("In front of you are three doors. "
                "There is a red door, a yellow door and a green door")
    print_pause("You must choose a door")


def green_door():
    if "handle" in items:
        print_pause("You have already been in "
                    "this room and there is nothing more to do here.")
        print_pause("You leave the room")
        choose_door()
    else:
        print_pause("You open the green door!")
        print_pause("You go inside")
        print_pause("The room is empty except for a table "
                    "which has a crank shaft handle on it")
        print_pause("You pick up the handle and exit the room")
        items.append("handle")
        choose_door()


def red_door():
    print_pause("You go to open the red door")
    if "red key" in items:
        print_pause("The door does not open, its locked")
        print_pause("Luckily, you have been to the "
                    "yellow room and have the key from the box")
        print_pause("You use the key and enter the room")
        print_pause("Inside the room, you find a staircase that leads up")
        print_pause("You have nowhere else to go so you take the stairs")
        level2()
    else:
        print_pause("The door does not open, its locked")
        print_pause("You remember your bronze key "
                    "and try it in the lock but it does not work")
        print_pause("You can't get in and have to choose another door")
        items.append("tried red door")
        choose_door()


def yellow_door():
    if "is open" not in items:
        print_pause("You go to open the yellow door, "
                    "you push on the handle and but its locked.\n "
                    "It looks like it needs a key. "
                    "You remember the bronze key and try it. \n"
                    "The door unlocks and you can go in")
        items.append("is open")
    else:
        print_pause("The door is unlocked")
    print_pause("You enter the room")
    print_pause("Inside the room you find an old man sitting "
                "at an oak desk reading a book with a bronze clasp")
    print_pause("He looks up and you and asks,\'Can I help you\'")
    convo = valid_input_convo("what is you response. Select 1, 2 or 3\n"
                              "1. Nothing\n"
                              "2. Yes please, Im lost and don\'t "
                              "know where to go. Can you help me?\n"
                              "3. No, you are too old to help me\n", numbers)
    if convo == '1':
        print_pause("The old man smiles and"
                    "goes back to reading his book")
        print_pause("You leave the room")
        choose_door()
    elif convo == '2':
        if "red key" in items:
            print_pause("Old man, \'You already have all I can offer\'.")
            print_pause("You have to leave the room")
            choose_door()
        else:
            print_pause("He closes his book and offers you a seat")
            action = valid_choices("Do you sit? Yes/No\n", choices).lower()
            if action == "yes":
                old_man_convo()
            elif action == "no":
                print_pause("The old man says goodbye and you leave the room")
                choose_door()
    elif convo == '3':
        print_pause("The old man laughs at you")
        print_pause("\'You are very rude, I don\'t "
                    "think this room is for you\', he says")
        print_pause("He waves his hand at you "
                    "and you are thrown out the room")
        if "handle" in items:
            print_pause("As the door closes the old man shouts, "
                        "\'I have taken back what you found, "
                        "you must start again\'")
            items.remove("handle")
            choose_door()
        else:
            choose_door()


def old_man_convo():
    print_pause("You sit down and the old "
                "man pulls a box from under the table")
    print_pause("He tells you your answers are in the "
                "box but you must have the key")
    print_pause("The box is made of bronze, "
                "you remember your bronze key and try to open the box")
    print_pause("You realise that there is no keyhole on the box "
                "but there is a small round hole on the side. "
                "You wonder what it could be")
    if "handle" in items:
        print_pause("You remember that you found "
                    "the crank handle in the green room")
        print_pause("You try to fit it on the side and it works")
        print_pause("You crank the box and, "
                    "after a short time, the lid pops open")
        print_pause("Inside the box you find a red key")
        items.append("red key")
        if "tried red door" in items:
            print_pause("You remember the red door is locked.")
        else:
            print_pause("You remember seeing a red door")
        print_pause("You leave the room")
        choose_door()
    else:
        print_pause("You can't open the box and have to leave the room")
        choose_door()


def choose_door():
    # doors = ["red", "green", "yellow"]
    choose_input = valid_input_door("which door "
                                    "do you choose?\n", doors).lower()
    if "green" in choose_input:
        green_door()
    elif "red" in choose_input:
        red_door()
    elif "yellow" in choose_input:
        yellow_door()


def level1():
    intro()
    choose_door()


def battle():
    your_score = 0
    goblin_score = 0
    battle_point = [5, 10, 20, 50]
    print_pause("You attack with your dagger")
    print_pause("You score")
    your_score += random.choice(battle_point)
    print_pause(your_score)
    print_pause("The Goblin scores")
    goblin_score += random.choice(battle_point)
    print_pause(goblin_score)
    if your_score > goblin_score:
        print_pause("You won.")
        print_pause("You breath a sigh and relief and continue")
        print_pause("You get to the top of the stairs "
                    "and see an exit. You escape!")
        play_again()
    elif your_score == goblin_score:
        print_pause("It's a draw!")
        fight_again = valid_choices("would you like to "
                                    "fight again?"
                                    " Yes or No\n", choices).lower()
        if fight_again == "yes":
            battle()
        elif fight_again == "no":
            print_pause("You have to go back to the previous level")
            print_pause("you must choose a door again")
            choose_door()
    else:
        print_pause("You lost.")
        fight_again = valid_choices("would you like to "
                                    "fight again?"
                                    " Yes or No\n", choices).lower()
        if fight_again == "yes":
            battle()
        elif fight_again == "no":
            print_pause("You have to go back to the previous level")
            print_pause("you must choose a door again")
            list.clear(items)
            choose_door()


def goblin_fight():
    print_pause("You reach the top of the stairs and get attacked by a goblin")
    print_pause("You have to attack the goblin or run away\n")
    fight_flight = valid_fight_choices("What do you choose? attack "
                                       "or run\n", fight_choices).lower()
    if "attack" in fight_flight:
        battle()
    elif "run" in fight_flight:
        print_pause("You run back down the stairs to the first room!")
        print_pause("you must choose a door again")
        list.clear(items)
        choose_door()


def play_again():
    play_more = valid_choices("Would you like to play "
                              "again? Yes or No\n", choices)
    if play_more == "yes":
        list.clear(items)
        level1()
    elif play_more == "no":
        print_pause("Thanks for playing")


def level2():
    goblin_fight()


level1()
