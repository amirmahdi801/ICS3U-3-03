from random import randint
while True :
    print ("welcome to rock paper and scissor game")
    user = input("please choose: 1.rock 2.paper 3.scissor: ")
    
    pc = randint(1, 3)
    pc = str(pc)

    rock = "1"
    paper = "2"
    scissor = "3"
    
    rock = "rock"
    paper = "paper"
    scissor = "scissor"
    
    if user == "1":
        print ("you chose rock")
    elif user == "2":
        print ("you chose paper")
    elif user == "3":
        print ("you chose scissor")
    else :
        print ("wrong input")
        exit()

    if pc == "1":
        pc = rock
    elif pc == "2":
        pc = paper
    elif pc == "3":
        pc = scissor
    
    print ("Computer is " + pc)
    
    if user == rock :
        if pc == paper :
            print ("you lose")
        elif pc == scissor :
            print ("you win")
        else :
            print ("Draw")
    elif user == "2" :
        if pc == rock :
            print ("you win")
        elif pc == scissor :
            print ("you lose")
        else:
            print ("Draw")
    elif user == "3" :
        if pc == rock :
            print ("you lose")
        elif pc == paper :
            print ("you win")
        else :
            print ("Draw")