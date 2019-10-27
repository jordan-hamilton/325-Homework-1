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
        sortedNumbers = mergeSort(toSort)
        algorithmTime = process_time() - algorithmTime
        printResults(sample, algorithmTime)


# Merge function adapted from Cormen, p. 34 and the week 1 induction proof video
def mergeSort(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        left = numbers[:len(numbers) // 2]
        right = numbers[len(numbers) // 2:]

        return merge(mergeSort(left), mergeSort(right))


# Merge function adapted from Cormen, p. 31 and the week 1 induction proof video
def merge(left, right):
    i = j = 0
    temp = []

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    while i < len(left):
        temp.append(left[i])
        i += 1
    while j < len(right):
        temp.append(right[j])
        j += 1

    return temp


if __name__ == "__main__":
    main()
