import random # For generating the unsorted list
import time as t

def insertion_sort(arr):
    for i in range(1, len(arr)): # Go through the length of the list
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]: # Find the correct position
            arr[j + 1] = arr[j] # Shift to the right
            j -= 1
        arr[j + 1] = key # Insert in the correct position

if __name__ == "__main__":
    # Generate a list of 10 random terms
    list = [random.randint(0, 10) for _ in range(10)]

    print("Unsorted List:", list)
    time = t.time()
    insertion_sort(list)
    print("Sorted List: ", list, "\nIt took: ", t.time() - time)
