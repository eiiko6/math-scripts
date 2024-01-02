# Mastermind

# ToDo: add a custom difficulty, add a combo system

# There are still things to be done, like implementing support for duplicates

import random

rounds = 0
score = 0


# Tool functions
def duplicates(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False


# Game functions
def askMode():
    TURNS = 0
    PEGS = ["A", "B", "C", "D", "E", "F"]
    CHAIN_LENGTH = 0

    print("Choose the game mode: \n",
          "- 1: Easy (4 characters code, 6 pegs, 10 turns) \n",
          "- 2: Medium (4 characters code, 7 pegs, 8 turns) \n",
          "- 3: Hard (4 characters code, 8 pegs, 7 turns) \n",
          "- 4: Harder (4 characters code, 8 pegs, 5 turns)",
          #"- 5: Custom (in development)"
    )
    mode = input("> ")

    while 1:
        if mode == "1":
            TURNS = 10
            CHAIN_LENGTH = 4
            return [1, TURNS, PEGS, CHAIN_LENGTH]
        
        elif mode == "2":
            TURNS = 8
            CHAIN_LENGTH = 4
            PEGS.append("G")
            return [2, TURNS, PEGS, CHAIN_LENGTH]
        
        elif mode == "3":
            TURNS = 7
            CHAIN_LENGTH = 4
            PEGS.append("G", "H")
            return [3, TURNS, PEGS, CHAIN_LENGTH]
        
        elif mode == "4":
            TURNS = 8
            CHAIN_LENGTH = 4
            PEGS.append("G", "H")
            return [4, TURNS, PEGS, CHAIN_LENGTH]
        
        elif mode == "5":
            TURNS = 10 # int(input("Enter the amount of turns > "))
            CHAIN_LENGTH = 4 # int(input("Enter the length of the code > "))
            # PEGS, string to array
            return [0, TURNS, PEGS, CHAIN_LENGTH]
        
        else:
            print("Please enter a correct input.")
            mode = input("> ")

def roll(allowDupes, PEGS, CHAIN_LENGTH): # Define a random solution
    if allowDupes:
        output = random.choices(PEGS, k=CHAIN_LENGTH) # With duplicates
    else:
        output = random.sample(PEGS, k=CHAIN_LENGTH) # Without duplicates

    return output

def checkInput(attempt, solution, PEGS, CHAIN_LENGTH): # Check if the input is legal and correct and return stuff
    # The returned values here are kinda "codeGuessed", "message" and "countsAsTry"... I know it's messy
    if attempt == '':
        return [False, "Input was empty.", False]
    elif not set(attempt).issubset(''.join(PEGS)): # If there are invalid characters
        return [False, "Please enter valid characters.", False]
    elif len(attempt) != CHAIN_LENGTH:
        return [False, "Invalid string length.", False]
    elif duplicates(attempt):
        return [False, "Duplicates aren't allowed.", False]
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


def game(TURNS, PEGS, CHAIN_LENGTH, mode): # Game here
    round_score = 10
    turns = TURNS
    solution = roll(False, PEGS, CHAIN_LENGTH) # Kinda broken if True

    print(f"Debug: {solution}") # Just for simplifying debug

    print("Game ready, try guessing the code!")
    print("The code is ", CHAIN_LENGTH, " characters long.")
    print("The valid pegs are", ", ".join(PEGS), "\n")
    
    while 1: # Ask for the input until it's correct or the turns are used up
        attempt = input("> ").upper()
        print(checkInput(attempt, solution, PEGS, CHAIN_LENGTH)[1])

        if checkInput(attempt, solution, PEGS, CHAIN_LENGTH)[0] == False:
            if checkInput(attempt, solution, PEGS, CHAIN_LENGTH)[2] == True:
                round_score -= 1
                turns -= 1
                print("Turns remaining: ", turns, "\n")

            if turns == 0:
                print("You used all of your turns!")
                print("The solution was: ", solution)
                round_score = 0
                break
        
        if checkInput(attempt, solution, PEGS, CHAIN_LENGTH)[0] == True:
            break
    
    if mode[0] == 2:
        round_score += 2
    elif mode[0] == 3:
        round_score += 3
    elif mode[0] == 4:
        round_score += 4

    print("Turns used: ", TURNS - turns + 1)
    print("You scored: ", round_score)

    again = True if input("Another round? (y/n) > ").lower() == 'y' else False
    print("\n- - - - - - - - -\n")

    return [round_score, again]


if __name__ == "__main__":
    mode = askMode()

    TURNS = mode[1]
    PEGS = mode[2]
    CHAIN_LENGTH = mode[3]

    print("\n", "Round: ", rounds)
    print("Total score: ", score)

    results = game(TURNS, PEGS, CHAIN_LENGTH, mode) # Run the game for the first time
    rounds += 1

    score += results[0]

    while 1:
        print("Round: ", rounds)
        print("Total score: ", score, "\n")

        if results[1] == True:
            results = game(TURNS, PEGS, CHAIN_LENGTH, mode) # Run the game
            rounds += 1
            score += results[0]
        else:
            break
