def sum_weights(weight_bop, weight_beep):
    total_weight = weight_bop + weight_beep
    return total_weight

def calc_avg_weight(weight_bop, weight_beep):
    total_avg_weight = (weight_bop + weight_beep) / 2
    return total_avg_weight

def run ():
    print("Please enter weight for Beep?")
    beep = float(input())
    print("Please enter weight for Bop?")
    bop = float(input())
    print("What would you like to print?(sum or avg)")
    action = input()

    if action == "sum" or "summery":
        answer = sum_weights(bop, beep)
        print(f"The sum of both bots bots is:{answer}.")
    elif action == "avg" or "average":
        answer = calc_avg_weight(bop, beep)
        print(f"the avg of both bots bots is:{answer}.")
    else:
        print("I am not sure what you would like to do.")
# Run program
run()


