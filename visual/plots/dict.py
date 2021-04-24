# Data Dictionary and Plots
import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}
    print("What type of line would you like (:, -- or -) ")
    user_type = input()

    print("What color would you like (r, g or b) ")
    user_color = input()

    print("What style of marker would you like (o, s or ^) ")
    user_style = input()

    paths['user_type'] = user_type
    paths['user_color'] = user_color
    paths['user_style'] = user_style

    return paths


def generate():
    print("How many lines would you like to display?")
    lines = int(input())

    for line in range(lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['user_type']}{values['user_color']}{values['user_style']}"
        plt.plot(x, y, format)

    plt.show()


def run():
    print("Running....")
    generate()
    print("Done!")


run()
