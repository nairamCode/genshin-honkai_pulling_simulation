import random

#letting the user input the probabilities
prob_5star = float(input("What's the Probability for an 5 star getting pulled?: "))
prob_4star = float(input("What's the Probability for an 4 star getting pulled?: "))
prob_3star = 100 - prob_5star - prob_4star

#letting the user input the amount of pulls after an object is guaranteed
guaranteed_5star = float(input("When is an 5 star guaranteed?: "))
guaranteed_4star = float(input("When is an 4 star guaranteed?: "))

#letting the user input the amount of Pulls he want to simulate
pull_amount = float(input("How many pulls do you want to simulate?: "))

#creating two lists for the pulls
five_star_pulls = []
four_star_pulls = []

#start the counters from the beginning (0)
counter = 0
pulled_5star = 0
pulled_4star = 0
pitty_5star = 0
pitty_4star = 0

#starting the loop to draw the objects
while True:
    #creating a list for the possible outcomes and a var to chose an option random
    counter = counter + 1
    mylist = ["5 star", "4 star", "3 star"]
    x = random.choices(mylist, weights=[float(prob_5star), float(prob_4star), float(prob_3star)], k=1)

    #count up and reset the pitty when a five star is drawed
    if x == ['5 star']:
        pulled_5star = pulled_5star + 1
        five_star_pulls.append(pitty_5star + 1)
        pitty_5star = 0
    #else count the pitty one up
    else:
        pitty_5star = pitty_5star + 1
        #if the pitty reaches the guarenteed amount draw an object
        if pitty_5star == float(guaranteed_5star):
            pulled_5star = pulled_5star + 1
            pitty_5star = 0

    #count up and reset the pitty when a four star is drawed
    if x == ['4 star']:
        pulled_4star = pulled_4star + 1
        four_star_pulls.append(pitty_4star + 1)
        pitty_4star = 0
    #else count the pitty one up
    else:
        pitty_4star = pitty_4star + 1
        #if the pitty reaches the guarenteed amount draw an object
        if pitty_4star == float(guaranteed_4star):
            pulled_4star = pulled_4star + 1
            pitty_4star = 0

    #stop if the entered amount to simulate is reached
    if counter == float(pull_amount):
        break

    #shows an percentage for how far the simulation is
    print(str(round(counter/pull_amount, 2) * 100) + "%", end='')
    print("\r", end='')

counter2 = 0
counter3 = 0

print("\n")
print("-----4 Star Pulls-----")

text = "Pulls: "

#print the results for the simulation
while True:
    fi = five_star_pulls.count(counter2 + 1)
    fo = four_star_pulls.count(counter3 + 1)

    #print a table for the 4 star pulls
    if counter3 < float(guaranteed_4star):
        print(f'{counter3 + 1:2}' + " " + f'{text}' + " " + f'{fo}')
        counter3 = counter3 + 1
        continue

    #print the average for pulling 4 star objects
    if counter2 == 0:
        print("\n", end='')
        print("Average Pulls to draw:")
        print(f'{round(counter / pulled_4star, 0):3}' + " (" + f'{counter / pulled_4star}' + ")")
        print("\n", end='')
        print("-----5 Star Pulls-----")

    #print a table for the 5 star pulls
    if counter2 < float(guaranteed_5star):
        print(f'{counter2 + 1:2}' + " " + f'{text}' + " " + f'{fi}')
        counter2 = counter2 + 1
        continue
    #print the average for pulling 5 star objects
    else:
        print("\n", end='')
        print("Average Pulls to draw:")
        print(f'{round(counter / pulled_5star, 0):4}' + " (" + f'{counter / pulled_5star}' + ")")
        break