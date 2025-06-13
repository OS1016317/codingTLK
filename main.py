import random

def get_user_choice():
    """Prompt the user for input and return their choice in uppercase."""
    return input("Please choose your next move (R, P, S) or Q to Quit: ").upper()

def get_cpu_choice():
    """Randomly select and return the CPU's choice."""
    return random.choice(['R', 'P', 'S'])

def determine_winner(user, cpu):
    """Determine the outcome of the round."""
    if user == cpu:
        return 'tie'
    elif (user == 'R' and cpu == 'S') or \
         (user == 'P' and cpu == 'R') or \
         (user == 'S' and cpu == 'P'):
        return 'win'
    else:
        return 'loss'

def display_result(user, cpu, outcome, name_map):
    """Print the result of the round."""
    print(f"You chose {name_map[user]}, CPU chose {name_map[cpu]}.")
    if outcome == 'tie':
        print("It's a tie!")
    elif outcome == 'win':
        print("You win!")
    else:
        print("CPU wins!")

def print_stats(wins, losses, ties):
    """Display the current game statistics."""
    print(f'Current Stats: {wins} Wins, {losses} Losses, {ties} Ties\n')

def play_game():
    """Main game loop."""
    wins, losses, ties = 0, 0, 0
    name_map = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    while True:
        user_choice = get_user_choice()

        if user_choice == 'Q':
            print("Thanks for playing!")
            break
        elif user_choice not in name_map:
            print("Invalid command. Please enter R, P, S, or Q.")
            continue

        cpu_choice = get_cpu_choice()
        outcome = determine_winner(user_choice, cpu_choice)
        display_result(user_choice, cpu_choice, outcome, name_map)

        if outcome == 'win':
            wins += 1
        elif outcome == 'loss':
            losses += 1
        else:
            ties += 1

        print_stats(wins, losses, ties)

# Run the game
play_game()
