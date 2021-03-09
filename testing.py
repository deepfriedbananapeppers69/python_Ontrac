import random 
score = 1
while score > 0:
    SoCal = ["ANA","PSP","BNS","LAX","BUR","ONT","COM","ORG","CPT","SAN","CXL","SMX","FON","VNS","HBC","WHP","JPD","YUM","JSG"]
    NoCal = ["CCR","PET","EUR","RED","HAY","SAC","MLO","SFO","MRY","SJC","STK"]
    socal = SoCal
    nocal = NoCal
    fullList = SoCal + NoCal
    choice = random.choice(fullList)
    print(choice)
    answer = input("socal or nocal: ")
    if "socal" in answer:
        answer = socal
    else:
        answer = nocal

    if choice in answer:
        print("correct")
        score = score + 1
        print("Your score is: " + str(score))
    else:
        print("not correct")
        score = score - 1
        print("Your score is: " + str(score))

