# Python stuff

## Introduction

Here's a colletion of random Python scripts that I made. They're usable but sometimes very specific.

## Scripts

### Math-related scripts:
<details>
    <summary>(read)</summary>

- ### [algebraicToTrigonometric.py](./Scrpits/math/algebraicToTrigonometric.py)   
    This script converts a complex number's algebraic expression to its trigonometric form.   
    The `convert` function takes 2 arguments that define the `reNumber` and `imNumber`.

- ### [concentricCircles.py](./Scrpits/math/concentricCircles.py)
    This script asks for user input and calculates the area of concentric circles.
    The radiuses can either have the same distance between them, or be specified individually.
    The user is warned if the values provided aren't sorted correctly.
</details>

### Sorting algorithms:
<details>
    <summary>(read)</summary>

- ### [bogo_sort.py](./Scripts/sorting-algorithms/bogo_sort.py)   
    This script implements the bogo sort algorithm. It shuffles the list randomly until it is sorted.

- ### [insertion_sort.py](./Scripts/sorting-algorithms/insertion_sort.py)   
    This script implements the insertion sort algorithm. It sorts the list by gradually building a sorted part of the list.

- ### [selection_sort.py](./Scripts/sorting-algorithms/selection_sort.py)
    This script implements the selection sort algorithm. It sorts the list by repeatedly finding the smallest element and putting it at the beginning.
</details>

### Games or other fun scripts:
<details>
    <summary>(read)</summary>

- ### [mastermind.py](./Scrpits/fun-games/mastermind.py)
    This is a simple mastermind game. Some parameters can be changed, like the amount of different pegs available, the sequence length or the amount of allowed tries. A score is added to a counter depending on the amount of turns used. Some common input errors like wrong characters or wrong length are handeled.
    For now duplicates in inputs aren't available and return an error.
    The game also has a difficulty level choice that affects the score gained.
    A custom difficulty should be added as well as a combo system.

- ### [coinChoice.py](./Scrpits/fun-games/coinChoice.py)   
    This scripts chooses an item from a list.    
    But the twist it that it does it by flipping a coin (represented by `random.randint(0, 1)`)    
    It divides the list in two until it only contains one element. But this means that it's not completely random: for that reason we first have to shuffle the list with `random.shuffle(items)` but it kind of ruins the point of only doing it with a coin toss.
</details>
