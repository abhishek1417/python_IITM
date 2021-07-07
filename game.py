# GAME :- rock beats scissors, scissors beat paper, paper beat rock


import random as r

choices = ['rock','paper', 'scissors']
computer= r.choice(choices)
print(computer)
computer_score = 0
human_score = 0
player = False

# Business logic of this game 
while True:
    player = input ("rock, paper or scissors ? :")
    if player == computer:
        print("DRAW MATCH :-(")
    elif player == 'rock':
        if computer =="paper":
            print("You Loose !")
            computer_score += 1
        else:
            print("You win !")
            human_score += 1
            
    elif player == 'paper':
        if computer =="scissors":
            print("You Loose !")
            computer_score += 1
        else:
            print("You win !")
            human_score += 1
            
    elif player == 'end':
        print("Total Score # ")
        print("Computer Score # ", computer_score)
        print("Human Score # ", human_score)
        break
