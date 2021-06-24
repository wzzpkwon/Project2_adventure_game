import time
import random
import sys


# function to print messages with pause.
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# function to validate input.
def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if response in option:
                return response


# function to print introductions for the game.
def intro():
    print_pause("In the middle of a dead-silent night, "
                "you are standing in the lobby of a building.")
    print_pause("You have been waiting for this day, "
                "to pull off a bank robbery!")
    print_pause("Geared up completely in black, "
                "you successfully infiltrated into the targeted bank.")
    print_pause("")
    print_pause("In front of you is the vault that is firmly shut.")
    print_pause("To your right is the security system control panel.")
    print_pause("To your left is a computer.\n")


# function to return to the lobby prior to take next course of action.
def to_lobby(tasks, options, passcodes):
    print_pause("You return to the lobby.")
    bank_robbery(tasks, options, passcodes)


# function to work on control panel for security devices.
def control_panel(tasks, options, passcodes):
    print_pause("You approach the control panel "
                "to deactivate the alarm and surveillance cameras.")
    if "deactivate" in tasks:
        print_pause("The security devices are already inactive. "
                    "You no longer have any business here.")
    else:
        print_pause("You have deactivated security devices. "
                    "Now you can move around the premises unhindered. ")
        tasks.append("deactivate")
    to_lobby(tasks, options, passcodes)


# function to hack the computer and download security codes.
def hack_computer(tasks, options, passcodes):
    print_pause("You approach the computer.")
    if "security_code" in tasks:
        print_pause("You already have the security code. "
                    "No need to stick around.")
        to_lobby(tasks, options, passcodes)
    else:
        if "deactivate" in tasks:
            print_pause("You’ve hacked the computer and "
                        "downloaded the security code.")
            print_pause(f"The security code you downloaded is {passcodes}")
            tasks.append("security_code")
            to_lobby(tasks, options, passcodes)
        else:
            print_pause("The alarm sets off as you "
                        "attempt to use the computer.")
            print_pause("Oh no! You have been detected "
                        "by the security camera!")
            play_again(options)


# function to work on vault door.
def open_vault(tasks, options, passcodes):
    print_pause("You approach the vault.")
    print_pause("It seems you need some kind of code "
                "to access the vault.")
    print_pause("Would you like to 1) enter the security code or "
                "2) crack the vault?")
    response = valid_input("(Please enter 1 or 2)\n", ['1', '2'])
    if response == "1":
        if "deactivate" in tasks:
            if "security_code" in tasks:
                enter_passcode = input("Please enter the security code:\n")
                if enter_passcode == passcodes:
                    print_pause("The vault door finally opens up.")
                    print_pause("You've made yourself into the vault "
                                "full of cash! Congratulations!")
                else:
                    print_pause("The alarm sets off "
                                "as you have entered a wrong password.")
                    print_pause("You are busted!")
                play_again(options)
            else:
                print_pause("You don’t have the security code "
                            "to access the vault.")
                to_lobby(tasks, options, passcodes)
        else:
            print_pause("The alarm sets off as you attempt "
                        "to enter the security code.")
            print_pause("You forgot to deactivate "
                        "the security devices...")
            print_pause("You are busted!")
            play_again(options)
    elif response == "2":
        if "deactivate" in tasks:
            print_pause("You miraculously cracked the vault door open.")
            print_pause("With sheer delight and sense of accomplishment, "
                        "you step into the vault.")
            print_pause("Suddenly, a hidden trap door appears and "
                        "locks you up inside the vault.")
            print_pause("Oh no, you are trapped!")
        else:
            print_pause("The alarm sets off as you attempt to "
                        "force your entry.")
            print_pause("You are busted!")
        play_again(options)


# function to select appropriate protocol for a bank heist!
def bank_robbery(tasks, options, passcodes):
    print_pause("Enter 1 to access control panel\n"
                "Enter 2 to use computer\n"
                "Enter 3 to go to the vault")
    print_pause("what would you like to do?")
    response = valid_input("(Please make a valid selection)\n", options)
    if response == "1":
        control_panel(tasks, options, passcodes)
    elif response == "2":
        hack_computer(tasks, options, passcodes)
    elif response == "3":
        open_vault(tasks, options, passcodes)


# function to ask the player to give options to replay or exit the game.
def play_again(options):
    response = valid_input("Would you like to play again? (y/n)", options)
    if response == "n":
        print_pause("Enough for the day, huh? Thanks for playing!")
    elif response == "y":
        print_pause("Great! Please wait while the game is restarting...")
        main()
    else:
        print_pause("Please enter a valid input: ")


# main function that executes the game.
def main():
    tasks = []
    options = ['1', '2', '3', 'y', 'n']
    passcodes = str(random.randrange(1000, 10000))
    intro()
    bank_robbery(tasks, options, passcodes)


if __name__ == '__main__':
    main()
    sys.exit()
