# Random Module
import random

print('Hello in \"Rock, Paper and Scissors\" game. \n')
print('------------------> Good Luck & Have Fun <------------------\n\n\n\n')
player_score = 0
computer_score = 0
while player_score < 3 or computer_score < 3:
    player_move = int(input("What you chose? \"1\" - rock, \"2\" - paper or \"3\" - scissors. -> "))
    computer_move = random.randint(1, 3)


    # Rock - 1
    print('------------------> You chose: <------------------')
    if player_move == 1:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

    # Paper - 2
    elif player_move == 2:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

    # Scissors - 3
    elif player_move == 3:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    else:
        print("Game Over :(")

    print('------------------> Computer chose: <------------------')
    if computer_move == 1:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

    # Paper - 2
    elif computer_move == 2:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

    # Scissors - 3
    elif computer_move == 3:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    else:
        print("Game Over :(")

    if computer_move == player_move:
        print("Draw!")
    elif computer_move == 1 and player_move == 3:
        print("Computer win!")
        computer_score += 1
    elif computer_move == 1 and player_move == 2:
        print("Player win!")
        player_score += 1
    elif computer_move == 2 and player_move == 1:
        print("Computer win!")
        computer_score += 1
    elif computer_move == 2 and player_move == 3:
        print("Player win!")
        player_score += 1
    elif computer_move == 3 and player_move == 1:
        print("Player win!")
        player_score += 1
    elif computer_move == 3 and player_move == 2:
        print("Computer win!")
        computer_score += 1
    print(f"You: {player_score}, computer: {computer_score}")
    if computer_score == 3:
        print("Computer win!")
        quit()
    if player_score == 3:
        print("Player Win!")
        quit()