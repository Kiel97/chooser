import keyboard
import random
import sys

def main():

    # Prepare variables
    amount = 0
    opts = []
    content = []

    # Start application and get path to file with options
    print("Hello World! Chooser is here to help you choose something from list!")

    filepath = input("Enter file name of your list of items to choose from: ")

    # Read title in first line, then read options and remove whitespaces around them
    with open(filepath, "r") as file:
        title = file.readline().strip()
        for line in file.readlines():
            content.append(line.strip())

    size = len(content)

    print("\nLoaded %d options to choose from." % size)

    # Allow only from 1 to amount of options minus 1
    while (is_invalid_amount(amount, size)):
        amount = int(input(("How many options you want to be chosen: ")))

        if (is_invalid_amount(amount, size)):
            print("Invalid value (%d). Try again!" % amount)
    
    print("Press Spacebar to stop randomizer...")
    while (True):
        # Empty selected and refill options arrays
        selected = []
        options = content[:]

        # Choose option, remove it from options and push it to selected
        # Print it to console
        for i in range(amount):
            s = random.choice(options)
            options.remove(s)
            selected.append(s)
            print(s)

        # Remove previous selected items (flashing text effect)
        for i in range(amount):
            clear_last_line()

        # Detect Spacebar press and stop randomizer
        # Print finally selected option(s)
        if keyboard.is_pressed('space'):
            clear_last_line()
            
            print("\n" + title)
            for item in selected:
                print(item)
            break

def clear_last_line():
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def is_invalid_amount(amount, size):
    return amount < 1 or amount >= size

main()