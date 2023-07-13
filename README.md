# Math Scripts

## Introduction

I like to put into python what I learn in math lessons.
So here are some small scripts i made. They're usable, but sometimes really specific...

## Scripts

- #### [algebraicToTrigonometric.py](https://github.com/mxstoto6/math-scripts/blob/main/Scrpits/algebraicToTrigonometric.py)   
    This script converts a complex number's algebraic expression to its trigonometric form.   
    The `convert` function takes 2 arguments that define the `reNumber` and `imNumber`.

- #### [coinChoice.py](https://github.com/mxstoto6/math-scripts/blob/main/Scrpits/coinChoice.py)   
    This scripts chooses an item from a list.    
    But the twist it that it does it by flipping a coin (represented by `random.randint(0, 1)`)    
    It divides the list in two until it only contains one element. But this means that it's not completely random: for that reason we first have to shuffle the list with `random.shuffle(items)` but it kind of ruins the point of only doing it with a coin toss.
