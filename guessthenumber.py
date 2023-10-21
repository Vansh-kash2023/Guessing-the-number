# Guessing the number
from collections import deque
import random

r=True
while r==True:
    print("Welcome to the Game of guessing the number. \n"+"You have to enter the minimum and the maximum value and then guess a number within its range. You will get 3 chances only. All the best. Lets begin...")
    a=int(input("Enter the minimum value: "))
    b=int(input("Enter the maximum value: "))
    l=deque()
    if a>b:
        print("Incorrect input.")
    else:
        for i in range(a,b+1):
            l.append(i)
        random_no=random.choice(l)
        c=1
        while c!=4:
            answer=int(input("Enter your answer: "))
            
            
            if answer<random_no:
                print("You guessed a lesser value. ")
            elif answer>random_no:
                print("You guessed a higher value. ")
            elif answer==random_no:
                print("wooaahh!! You guessed the correct value. You WON!! ")
                break
            else:
                pass
            if c==2:
                print("This is you last chance")
            
            c+=1
            
        if c == 4:
            print("Sorry, you've used all three chances. The correct number was:", random_no)
        
        x=input("Do you want to play again?(Y/N)")
        if x == "N"or x=="n":
            print("Game ended")
            r=False
            break
        elif x == "Y"or x=="y":
            r=True
            continue
        else:
            print("Invalid input.")