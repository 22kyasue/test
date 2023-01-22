# First Year Seminar B
# a basic rock paper scissor game
# Created by Keisuke Fukui

#importing module
import random 

#Game Starts Here
def damage(): 
    num_of_rounds = int(
        input("Welcome to a game of rock paper scissors. Enter the number of rounds you would like to play: "))
    if num_of_rounds == 0:
        print("Bye")
    else:

        while num_of_rounds >= 1:

            choices = ['rock', 'scissors', 'paper']

            print(f'The choices are {choices}')

            computer = random.choice(choices)
            player = None
            while player not in choices:
                player = input("What will be your hand?: ").lower()
            print(f'the computers hand is {computer}')

            if player == computer:
                print("tie")

            elif player == 'paper':
                if computer == 'rock':
                    print('You win')

                elif computer == 'scissors':
                    print("You lose")

            elif player == 'rock':
                if computer == 'scissors':
                    print('You win')
                elif computer == 'paper':
                    print("You lose")

            elif player == 'scissors':
                if computer == 'paper':
                    print('You win')
                elif computer == 'rock':
                    print("You lose")

            num_of_rounds -= 1

            if num_of_rounds == 0:
                prompt = input("Would you like to continue playing? Type yes or no: ").lower()
                if num_of_rounds == 0:
                    print("You have finished the entered number of rounds. Bye.")
                elif prompt != "yes":  # not equal to
                    print("bye")
                    break

# Calling the function
damage()
