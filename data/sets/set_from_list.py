def observed():
    observations =[]

    for count in range(7):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def run():
    print("Counting observations...")
    observations = observed()
    observation_set = set()

    for value in observations:
        data = (value, observations.count(value))
        observation_set.add(data)

    for data in observation_set:
        print(f"{data[0]} observed {data[1]} times.")
        print(observation_set)
        print(observations)
if __name__=="__main__":
    run()