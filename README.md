# Python stuff

## Introduction

I like writing random scripts that do random things.
So here are some small ones I made. They're usable, but sometimes really specific...

## Scripts

- ### [algebraicToTrigonometric.py](./Scrpits/algebraicToTrigonometric.py)   
    This script converts a complex number's algebraic expression to its trigonometric form.   
    The `convert` function takes 2 arguments that define the `reNumber` and `imNumber`.

- ### [coinChoice.py](./Scrpits/coinChoice.py)   
    This scripts chooses an item from a list.    
    But the twist it that it does it by flipping a coin (represented by `random.randint(0, 1)`)    
    It divides the list in two until it only contains one element. But this means that it's not completely random: for that reason we first have to shuffle the list with `random.shuffle(items)` but it kind of ruins the point of only doing it with a coin toss.

- ### [concentricCircles.py](./Scrpits/concentricCircles.py)
    This script asks for user input and calculates the area of concentric circles.
    The radiuses can either have the same distance between them, or be specified individually.
    The user is warned if the values provided aren't sorted correctly.
