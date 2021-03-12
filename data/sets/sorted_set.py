def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def remove_observations(observations):
    islooping = True

    while (islooping):
        print("Do you wish to remove an observation? (yes/no)?")
        response = input()

        if (response == "yes"):
            print("Please enter the observation you wish to remove")
            observation = input()
            observations.remove(observation)
        else:
            break
def run():
    observations = observed()
    remove_observations(observations)

    observation_set = set()
    for value in observations:
        data = (value, observations.count(value))
        observation_set.add(data)

    for data in sorted(observation_set):
        print(f"{data[0]} observed {data[1]} times.")

if __name__=="__main__":
    run()






