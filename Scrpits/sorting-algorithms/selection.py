import random as r
import time as t

# Sorting
def sort(l):
    for i in range(0, len(l)-1): # Go through the length of the list
        min = l[i]
        index = i

        # Find the minimum element in the unsorted part
        for j in range(i+1, len(l)):
            if l[j] < min:
                min = l[j]
                index = j

        # Swap with the first element
        hold = l[i]
        l[i] = l[index]
        l[index] = hold
    return l

if __name__ == "__main__":
    # Generate a list of 10 random terms
    list = [r.randint(1, 10) for _ in range(10)]

    time = t.time()

    # Print sorted list
    print(sort(list))
    print("It took: " + str(t.time() - time))
