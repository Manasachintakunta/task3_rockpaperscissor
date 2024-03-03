import random
def user_choice():
    while True:
        uchoice= input("Enter your choice(rock ,paper, scissor)").lower()
        if uchoice in ['rock','paper','scissor']:
            return uchoice
        else:
            print("Invalid choice")

def computer_choice():
    return random.choice(['rock','paper','scissor'])

def winner(uchoice,cchoice):
    if uchoice==cchoice:
        print("TIE")
    elif(uchoice=='rock' and cchoice=='scissor' or uchoice=='paper' and cchoice=='rock' or uchoice=='scissor' and cchoice=='paper'):
        return "YOU WIN"
    else:
        return "COMPUTER WINS"
def play_game():
    uchoice=user_choice()
    cchoice=computer_choice()
    print("computer choice:", cchoice)
    print(winner(uchoice,cchoice))
play_game()
