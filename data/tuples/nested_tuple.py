def steps():
    liklihoods=[
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]

    return liklihoods

def run():
    lh=steps()
    good_steps=[]
    bad_steps=[]

    for item in lh:

        if (item[1] >= 50):
            bad_steps.append(item)
        else:
            good_steps.append(item)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

if __name__=="__main__":
    run()
