def gang():
    print("Loading gang...")

    friends =["Scooby Doo",
            "Shaggy Rogers",
            "Fred Jones",
            "Daphne Blake",
            "Velma Dinkley"
    ]
    print(friends[0:4])

    print("...Done!")
    return friends


def phrases(friends):
    quotes = {}

    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()

    quotes = {f"{quote}:{friends}"}

    return quotes

friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")


def save(qoutes):
    quote = qoutes
    with open("quotes.txt", "w") as file:
        file.write("")

    for _ in qoutes:
        quotes_ = {f"\n {friends}:{quote}"}

save(quotes)
print("The file contains...")
file = open("quotes.txt")
print(file.read())
file.close()




