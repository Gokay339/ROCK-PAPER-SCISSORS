from random import choice

print("#" * 80)
print("#" * 30 + " Rock, Paper, Scissors " + "#" * 29)
print("#" * 29 + " Welcome to the Game " + "#" * 29)
print("#" * 80)
print("Press 'q' to Exit the Game.")

while True:
    print("""Choose the Option You Want to Play:\n
    1. Single Round
    2. First to 3 Wins\n""")

    try:
        game_choice = input("Option: ")

        if game_choice == "1" or game_choice == "2":
            game_choice = int(game_choice)
        elif game_choice == "q" or game_choice == "Q":
            print("Game Over...")
            exit()
        else:
            print("You made an invalid choice. Please enter '1' or '2' or 'q'.\n")
            continue
    except ValueError:
        print("You made an invalid choice. Please enter '1' or '2'.\n")
        continue

    while True:
        if game_choice == 1:
            computer_choice = choice(["rock", "paper", "scissors"])
            computer_choice = computer_choice.upper()
            print("Rock, Paper, Scissors - Enter Your Choice ")

            player_choice = str(input("Your Turn: "))
            player_choice = player_choice.upper()
            if player_choice != "ROCK" and player_choice != "PAPER" and player_choice != "SCISSORS" and player_choice != "Q":
                print("You made an invalid choice.\nPlease enter 'rock', 'paper', 'scissors', or 'q'.\n")
                continue

            if player_choice == "ROCK":
                if computer_choice == "ROCK":
                    print("Computer's Choice: Rock")
                    print("Result: Draw!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

                elif computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: You Lost!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

                else:
                    print("Computer's Choice: Scissors")
                    print("Result: You Won!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

            elif player_choice == "PAPER":
                if computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: Draw!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

                elif computer_choice == "ROCK":
                    print("Computer's Choice: Rock")
                    print("Result: You Won!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

                else:
                    print("Computer's Choice: Scissors")
                    print("Result: You Lost!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

            elif player_choice == "SCISSORS":
                if computer_choice == "SCISSORS":
                    print("Computer's Choice: Scissors")
                    print("Result: Draw!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

                elif computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: You Won!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

                else:
                    print("Computer's Choice: Rock")
                    print("Result: You Lost!\n")
                    print("""Do You Want to Play Again? 
    Press 'q' to Exit...\n""")

            elif player_choice == "Q":
                print("Game Over...")
                exit()

        if game_choice == 2:
            game_score = {"player": 0, "computer": 0}

            while True:
                computer_choice = choice(["rock", "paper", "scissors"])
                computer_choice = computer_choice.upper()
                print("Rock, Paper, Scissors - Enter Your Choice ")
                player_choice = str(input("Your Turn: "))
                player_choice = player_choice.upper()

                if player_choice != "ROCK" and player_choice != "PAPER" and player_choice != "SCISSORS" and player_choice != "Q":
                    print("You made an invalid choice.\nPlease enter 'rock', 'paper', 'scissors', or 'q'.\n")
                    continue

                if player_choice == "ROCK":
                    if computer_choice == "ROCK":
                        print("Computer's Choice: Rock")
                        print("Result: Draw!\n")
                    elif computer_choice == "PAPER":
                        print("Computer's Choice: Paper")
                        print("Result: You Lost!\n")
                        game_score['computer'] += 1
                    else:
                        print("Computer's Choice: Scissors")
                        print("Result: You Won!\n")
                        game_score['player'] += 1

                elif player_choice == "PAPER":
                    if computer_choice == "PAPER":
                        print("Computer's Choice: Paper")
                        print("Result: Draw!\n")
                    elif computer_choice == "ROCK":
                        print("Computer's Choice: Rock")
                        print("Result: You Won!\n")
                        game_score['player'] += 1
                    else:
                        print("Computer's Choice: Scissors")
                        print("Result: You Lost!\n")
                        game_score['computer'] += 1

                elif player_choice == "SCISSORS":
                    if computer_choice == "SCISSORS":
                        print("Computer's Choice: Scissors")
                        print("Result: Draw!\n")
                    elif computer_choice == "PAPER":
                        print("Computer's Choice: Paper")
                        print("Result: You Won!\n")
                        game_score['player'] += 1
                    else:
                        print("Computer's Choice: Rock")
                        print("Result: You Lost!\n")
                        game_score['computer'] += 1

                print(f"Scores  You: {game_score['player']}  and  Computer: {game_score['computer']}")

                if game_score['player'] == 3:
                    print("Game over!\nYou Win!")
                    exit()
                if game_score['computer'] == 3:
                    print("Game over!\nYou Lost!")
                    exit()

                elif player_choice == "Q":
                    print("Game Over...")
                    exit()
