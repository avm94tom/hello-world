dice1=['1','2','3','4','5','6']
dice2=['1','2','3','4','5','6']
result1=0
result2=0
turn=0
game_on=True

import random


from Tkinter import *
master=Tk()
w= Canvas(master,width = 200, height=300)
w.pack
mainloop()

while answer == "yes" or "Yes" or "YES" :
    result1=random.choice(dice1)
    result2=random.choice(dice2)
    print(result1)
    print(result2)
    turn+=1
    print("Let's play?")
    answer = input(str())
    if answer == "yes" or "Yes" or "YES":
        game_on=True
    else :
        game_on=False
