# Mastermind
import random, os

TURNS = 5
PEGS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
CHAIN_LENGTH = 4

rounds = 0
score = 0


def roll(allowDupes): # Define a random solution
    if allowDupes:
        output = random.choices(PEGS, k=CHAIN_LENGTH) # With duplicates
    else:
        output = random.sample(PEGS, k=CHAIN_LENGTH) # Without duplicates

    return output

def checkInput(attempt, solution): # Check if the input is legal and correct and return stuff
    # The returned values here are kinda "codeGuessed", "message" and "countsAsTry"... I know it's messy
    if attempt == '':
        return [False, "Input was empty.", False]
    elif not set(attempt).issubset(''.join(PEGS)): # If there are invalid characters
        return [False, "Please enter valid characters.", False]
    elif len(attempt) != CHAIN_LENGTH:
        return [False, "Invalid string length.", False]
    else:
        white_pegs = 0
        for peg in attempt:
            if peg in solution: # If a peg is present in the solution
                white_pegs += 1 
        
        black_pegs = 0
        for i, peg in enumerate(attempt):
            if peg == solution[i]:
                black_pegs += 1

        white_pegs -= black_pegs  # Exclude black pegs from white pegs

        if black_pegs == CHAIN_LENGTH:
            return [True, "Congratulations! You guessed the code!", True]
        else:
            return [False, f"Correct pegs in the right position: {black_pegs}, correct pegs in the wrong position: {white_pegs}", True]


def game(): # Game here
    round_score = 10
    turns = TURNS
    solution = roll(False)

    print(f"Debug: {solution}") # Just for simplifying debug

    print("Game ready, try guessing the code!")
    print("The valid pegs are", ", ".join(PEGS))
    
    while True: # Ask for the input until it's correct or the turns are used up
        attempt = input("> ")
        print(checkInput(attempt, solution)[1])

        if checkInput(attempt, solution)[0] == False:
            if checkInput(attempt, solution)[2] == True:
                round_score -= 1
                turns -= 1
                print("Turns remaining: ", turns)

            if turns == 0:
                print("You used all of your turns!")
                round_score = 0
                break
        
        if checkInput(attempt, solution)[0] == True:
            break

    print("\n")
    print("Turns used: ", TURNS - turns + 1)
    print("You scored: ", round_score)

    again = True if input("Another round? (y/n) > ").lower() == 'y' else False
    os.system('cls')

    return [round_score, again]



if __name__ == "__main__":
    os.system('cls')

    print("Round: ", rounds)
    print("Total score: ", score)

    results = game() # Run the game for the first time
    rounds += 1
    score += results[0]

    while True:
        score += results[0]
        print("Round: ", rounds)
        print("Total score: ", score)

        if results[1] == True:
            results = game() # Run the game
            rounds += 1
        else:
            break
