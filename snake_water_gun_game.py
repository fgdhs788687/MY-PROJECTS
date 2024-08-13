import random
"""
Following are the rules of the game:
    ->Snake vs. Water: Snake drinks the water hence wins.
    ->Water vs. Gun: The gun will drown in water, hence a point for water.
    ->Gun vs. Snake: Gun will kill the snake and win.

1 for snake
-1 for water
0 for gun     
"""
computer=random.choice([-1,0,1])
youstr=input("Enter your choice(s,w,g): ")
youdict={"s":1,"w":-1,"g":0}
compdict={1:"snake",-1:"water",0:"gun"}

you = youdict[youstr]

print(f"{compdict[you]}\n{compdict[computer]}")
if (computer==you):
    print("its a draw..")
else:    
    if computer==-1 and you==1:
        print("you win")
    elif computer==-1 and you==0:
        print("you lose")
    elif computer==1 and you==-1:
        print("you lose")
    elif computer==1 and you==0:
        print("you win")
    elif computer==0 and you==-1:
        print("you win")
    elif computer==0 and you==1:
        print("you lose")

        

