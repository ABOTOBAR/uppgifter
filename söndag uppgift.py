print("Welcome to treasure hunt game!")
print("This is game is about saving the queen elizabeth. So the king Amir ")

choice1 = input("do you want to go left or right? Just for you to know if you go left you will") 

if choice1 == "left":
    choise2 = input("You choise the right path! Now you se a river, will jump over or swim?")
    if choise2 == "jump":
        choise3 = input("You have now come to land, you are hungry, what are you looking for first, food or water")
        if choise3 == "water":
            choise4 = input("you see a dragon do you want to attack with fire, ice or wind magic")
            if choise4 == "Fire":
                input("Very good choise, The dragon took som seriously damage and died instantly!")
            elif choise4 == "Ice":
                input("Good choise, The dragon frozed to death instantly!")
                  choise5 = input("")




            else:
                print("Game Over")

        else:
            print("Game Over")

    else:
        print("Game Over")

else:
    print("Game Over")
