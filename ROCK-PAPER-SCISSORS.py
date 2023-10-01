from random import choice

# Printing a header for the game
print("#" * 80)
print("#" * 27 + "  Rock - Paper - Scissors  " + "#" * 26)
print("#" * 27 + "    Welcome to the Game    " + "#" * 26)
print("#" * 80)

print("To Quit the Game, Press q Key.")
while True:
    print("Choose an Option to Play\n"
          "1. Single Round\n"
          "2. Best of Three\n")
    try:
        game_choice = input("Choice: ")
        if game_choice == "1" or game_choice == "2":
            game_choice = int(game_choice)
        elif game_choice == "q" or game_choice == "Q":
            print("Game Over ...")
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
            print("Rock, Paper, or Scissors - Type Your Choice")

            player_choice = str(input("Your Turn: "))
            player_choice = player_choice.upper()
            if player_choice != "ROCK" and player_choice != "PAPER" and player_choice != "SCISSORS" and player_choice != "Q":
                print("You made an invalid choice.\nPlease enter 'rock', 'paper', 'scissors', or 'q'.\n")
                continue

            if player_choice == "ROCK":
                if computer_choice == "ROCK":
                    print("Computer's Choice: Rock")
                    print("Result: Tie!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

                elif computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: You Lose!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

                else:
                    print("Computer's Choice: Scissors")
                    print("Result: You Win!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

            elif player_choice == "PAPER":
                if computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: Tie!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

                elif computer_choice == "ROCK":
                    print("Computer's Choice: Rock")
                    print("Result: You Win!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

                else:
                    print("Computer's Choice: Scissors")
                    print("Result: You Lose!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

            elif player_choice == "SCISSORS":
                if computer_choice == "SCISSORS":
                    print("Computer's Choice: Scissors")
                    print("Result: Tie!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

                elif computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: You Win!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

                else:
                    print("Computer's Choice: Rock")
                    print("Result: You Lose!\n")
                    print("Do You Want to Play Again? Press 'q' to Quit ...\n")

            elif player_choice == "Q":
                print("Game Over ...")
                exit()

        if game_choice == 2:
            game_score = {"player": 0, "computer": 0}
            computer_choice = choice(["rock", "paper", "scissors"])
            computer_choice = computer_choice.upper()
            print("Rock, Paper, or Scissors - Type Your Choice")

            player_choice = str(input("Your Turn: "))
            player_choice = player_choice.upper()
            if player_choice != "ROCK" and player_choice != "PAPER" and player_choice != "SCISSORS" and player_choice != "Q":
                print("You made an invalid choice.\nPlease enter 'rock', 'paper', 'scissors', or 'q'.\n")
                continue

            if player_choice == "ROCK":
                if computer_choice == "ROCK":
                    print("Computer's Choice: Rock")
                    print("Result: Tie!\n")
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

                elif computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: You Lose!\n")
                    game_score['computer'] += 1
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

                else:
                    print("Computer's Choice: Scissors")
                    print("Result: You Win!\n")
                    game_score['player'] += 1
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

            elif player_choice == "PAPER":
                if computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: Tie!\n")
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

                elif computer_choice == "ROCK":
                    print("Computer's Choice: Rock")
                    print("Result: You Win!\n")
                    game_score['player'] += 1
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

                else:
                    print("Computer's Choice: Scissors")
                    print("Result: You Lose!\n")
                    game_score['computer'] += 1
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

            elif player_choice == "SCISSORS":
                if computer_choice == "SCISSORS":
                    print("Computer's Choice: Scissors")
                    print("Result: Tie!\n")
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

                elif computer_choice == "PAPER":
                    print("Computer's Choice: Paper")
                    print("Result: You Win!\n")
                    game_score['player'] += 1
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

                else:
                    print("Computer's Choice: Rock")
                    print("Result: You Lose!\n")
                    game_score['computer'] += 1
                    print(f" Scores  You : {game_score['player']}  and  Computer : {game_score['computer']}")

            if game_score['player'] == 3:
                print("Game Over!\nYou Win!")
                exit()
            if game_score['computer'] == 3:
                print("Game Over!\nYou Lose!")
                exit()

            elif player_choice == "Q":
                print("Game Over ...")
                exit()
