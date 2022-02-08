from secrets import choice
import time
import random


def print_dialog(dialog):
    print(dialog)
    time.sleep(1)


def play():
    inventory = random.choice(["assault rifle"])
    target = random.choice(["Tank", "Jet", "car"])
    intro(target, inventory)
    camp(target, inventory)
    battle(target, inventory)


def intro(target, inventory):
    print_dialog("You are on the medal of the battlefield, you can "
                 "see a lot of dead bodys on front of you!!!\n")
    print_dialog("You hear an order to destroy the " + target + ".\n")
    print_dialog("The " + target + " is coming to your location!!!\n")
    print_dialog("You can see a camp in your right.\n")
    print_dialog("You have " + inventory + " on your inventory\n")
    while True:
        choice1 = input("Would you like to (1) enter the camp or "
                        "(2) face the " + target + "? \n")
        if choice1 == ("2"):
            print_dialog("You went to face the " + target + "!!!\n")
            battle(target, inventory)
            break
        if choice1 == ("1"):
            print_dialog("You entered the camp.\n")
            camp(target, inventory)
            break


def camp(target, inventory):
    print_dialog("After you enterd the camp.\n")
    print_dialog("You found a wapens locker.\n")
    print_dialog("You ask your self should I open it?\n")
    while True:
        choice2 = input("Would you like to (1) open the Loker or "
                        "(2) face the " + target + "? \n")
        if choice2 == ("2"):
            print_dialog("You went to face the " + target)
            battle(target, inventory)
            break
        if choice2 == "1":
            print_dialog("You opened the Loker\n")
            print_dialog("You found anti aircraft gun and anti tank gun\n")
            print_dialog("You ask your self witch wapen should I pick?\n")
            while True:
                choice3 = input("Would you like to pickup (1)"
                                " Anti aircraft gun (2) Anti tank gun ? \n")
                if choice3 == "1":
                    print_dialog("You picked the aircraft this could be "
                                 "usefull on the jets\n")
                    print_dialog("You walk back to face the " + target +
                                 "!!!\n")
                    inventory.append("Anti aircraft gun")
                    battle(target, inventory)
                    break
                if choice3 == "2":
                    print_dialog("You picked the anti tank this"
                                 " could be usefull on the jetsz\n")
                    print_dialog("You walk back to face the " + target +
                                 "!!!\n")
                    inventory.append("Anti tank gun")
                    battle(target, inventory)
                    break


def battle(target, inventory):
    print_dialog("The " + target + "in front of you\n")
    print_dialog("Will you face the " + target + "?\n")

    while True:
        choice4 = input("Please enter (1) fight (2) to surrender \n")
        if choice4 == ("2"):
            print_dialog("You surrender\n")
            play_again()
            break
        if choice4 == ("1"):
            if target == "car" and "assault rifle" in inventory:
                print_dialog("The " + target + " attack you!!!\n")
                print_dialog("But with your Assault Rifle you"
                             "distroy the " + target + "!!!\n")
                print_dialog("You win this battle!!!\n")
                play_again()
                break
            if target == "Jet" and "Anti aircraft gun" in inventory:
                print_dialog("The " + target + " attack you!!!\n")
                print_dialog("But with your Anti aircraft gun"
                             " you distroy the " + target + "!!!\n")
                print_dialog("You win this battle!!!\n")
                play_again()
                break
            if target == "Tank" and "Anti aircraft gun" in inventory:
                print_dialog("The " + target + " attack you!!!\n")
                print_dialog("But with your Anti tank gun"
                             " you distroy the " + target + "!!!\n")
                print_dialog("You win this battle!!!\n")
                play_again()
                break
            else:
                print_dialog("The " + target + " attack you!!!\n")
                print_dialog("But your wapen is not enough"
                             " to distroy the " + target + "!!!\n")
                print_dialog("You died!!!\n")
                play_again()
                break


def play_again():
    while True:
        play_again = input("Want to play again? (yes/no)").lower()
        if play_again == "yes":
            print_dialog("Restarting the game ...\n")
            play()
            break
        if play_again == "no":
            print_dialog("\n\n\n\n\n\nThanks for playing!!!\n\n\n\n\n\n")
            exit()
            break


play()
