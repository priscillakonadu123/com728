def likelihood():
    likelihood = (50, 38, 27, 99, 4)
    min_value = min(likelihood)
    max_value = max(likelihood)
    return min_value, max_value

def run():
    min_value, max_value = likelihood()

    print(f"Minimum likelihood of falling: {min_value}%")
    print(f"Maximum likelihood of falling: {max_value}%")

    print(f"Maximum likelihood of falling: {likelihood()}%")

run()