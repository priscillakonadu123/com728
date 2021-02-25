def display_box(word):
    numbers = 4 + len(word)
    print("-"* numbers)
    print(f"~ {word} ~")
    print("-" * numbers)

def lower_case(word):
    print(word.lower_case())

def upper_case(word):
    print(word.upper_case())

def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")

def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(lower_case(word))
        # odd repetition
        else:
            print(upper_case(word))


def run():
    print("Please enter a word?")
    enter_word = input()

    print("Choose one of the following options or write a number (e.g. 1-5)")

    print("1" or "Display in a Box – display the word in an ascii art box")
    print("2" or "Display Lower-case – display the word in lower-case e.g. hello")
    print("3" or "Display Upper-case – display the word in upper-case e.g. HELLO")
    print("4" or "Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
    print("5" or "Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.")
    print("6" or "Quit")
    respond = input()

    if respond == 1:
        display_box(enter_word)
    elif respond == 2:
        lower_case(enter_word)
    elif respond == 3:
        upper_case(enter_word)
    elif respond == 4:
        display_mirrored(enter_word)
    elif respond == 5:
        display_repeated(enter_word)
    else:
        print("Unknown option.")