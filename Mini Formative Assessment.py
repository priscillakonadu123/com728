FUNCTION: COMMENCE

def commence():

    print("The Avengers Initiative")
    print("Please enter the number of days:")
    days = input()

    print(f"The Avengers Initiative will commence in {days} days.")

print()
commence()


FUNCTION: LEAD

def lead(leader):
    if leader == "Tony Stark":
        print("The Avengers are ready!")
    else:
        print("We need a better leader.")

lead("Hulk")

lead("Tony Stark")

FUNCTION: ASSEMBLE

def assemble(num_avengers):
    print("Assembling Avengers...")
    for count in range(0,num_avengers,1):
        print("...Avenger has assembled.")


assemble(3)


