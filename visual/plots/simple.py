import matplotlib.pyplot as plt


def display(x, y):
    plt.plot(x, y)


def run():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]

    x = x_values
    y = y_values

    display(x, y)

    plt.show()


run()
