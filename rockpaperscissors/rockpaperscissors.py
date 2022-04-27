import random
game_choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(game_choices)
player_choice = False
computer_score = 0
player_score = 0

while True:
    player_choice = input("Rock, Paper, or Scissors or End to end the game : ").capitalize()
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cuts ", player_choice)
            computer_score += 1
        else:
            print("You win!", player_choice, "covers ", computer_choice)
            player_choice += 1
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("You win!", player_choice, "smashes ", computer_choice)
            player_choice += 1
        else:
            print("You lose", computer_choice, "covers ", player_choice)
            computer_score += 1
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("You win!", player_choice, "cuts ", computer_choice)
            player_choice += 1
        else:
            print("You lose!", computer_choice, "smashes ", player_choice)
            computer_score += 1
    elif player_choice == 'End':
        print("a")
        print("Final Scores : ")
        print(f"Computer Score : {computer_score}")
        print(f"Player Score : {player_score}")
        break
