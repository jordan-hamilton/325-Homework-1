#!/usr/bin/env python3


from random import randint, seed
from time import process_time


# Provide clearer output on the amount of time spent processing the given number of elements
def printResults(size, algorithmTime):
    print('Array size: %d' % size)
    print('Processing time: %f seconds\n' % algorithmTime)


# Generate a specified number of integers between the minimum and maximum values, appending each number to a list and
# then return that list
def generateNumbers(size, minVal, maxVal):
    numList = []
    for i in range(size):
        numList.append(randint(minVal, maxVal))
    return numList


# Create a list of several list sizes to be filled with random numbers, then clock the processing time spend running
# the sort algorithm on each list and output the results
def main():
    seed()
    arraySize = [250, 500, 1000, 2500, 5000, 7500, 10000, 15000, 20000, 25000]
    for sample in arraySize:
        toSort = generateNumbers(sample, 0, 10000)
        algorithmTime = process_time()
        sortedNumbers = insertionSort(toSort)
        algorithmTime = process_time() - algorithmTime
        printResults(sample, algorithmTime)

# Insertion sort as adapted from psuedocode in Cormen, p. 18
def insertionSort(numbers):
    for j, key in enumerate(numbers[1:], start=1):
        i = j - 1
        while i >= 0 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            i -= 1
        numbers[i + 1] = key
    return numbers


if __name__ == "__main__":
    main()
