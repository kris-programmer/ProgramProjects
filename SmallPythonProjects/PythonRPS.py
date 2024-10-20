import random

choices = ('r', 'p', 's')
emojis = {'r':"🪨", 'p':"📄", 's':"✂️"}

def check_choices(player_choice, bot_choice):
    print(f"You chose {emojis[player_choice]}")
    print(f"Computer chose {emojis[bot_choice]}")

    if player_choice == bot_choice:
        print("It's a tie!")
    elif (
        (player_choice == 'r' and bot_choice == 's') or  
        (player_choice == 'p' and bot_choice == 'r') or 
        (player_choice == 's' and bot_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")

while True:
    try:
        player_choice = input("Rock, paper or scissors? (r/p/s): ").lower()
        bot_choice = random.choice(choices)
        check_choices(player_choice, bot_choice)
        
        print("")
        continue_game = input("Continue? (y/n): ").lower()
        if continue_game == 'y':
             continue
        else:
            break
    except ValueError:
        print("Invalid choice!")