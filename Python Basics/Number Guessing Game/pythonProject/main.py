import random


goagain=True
while goagain==True:
    try:
        pickedNum=random.randrange(1,10)
        numberGiven = int(input("Enter a number from 1 to 10: "))
        if(pickedNum==numberGiven):
            print("Congratulations you won!")
            anotherGame = input("Play again?(y/n): ")
            if(anotherGame!="y"):
                break
        else:
            print("Ohh next time better")
            anotherGame = input("Play again?(y/n): ")
            if (anotherGame != "y"):
                break


    except:
        print("Something went wrong....")
