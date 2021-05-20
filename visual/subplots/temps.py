import matplotlib.pyplot as plt


def read_data(file_path):
    file_list = []
    with open(file_path, 'r') as file:
        for line in file:
            file_list.append(float(line.strip()))
    return file_list


def run():
    data = read_data("temps.txt")
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()


run()
