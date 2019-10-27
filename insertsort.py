#!/usr/bin/env python3


# Open the file with the passed name as read only, using the readlines method to insert each line into a list, then
# return the created list.
def openFile(fileName):
    with open(fileName, 'r') as file:
        contents = file.readlines()
    return contents


# Append each element in the passed list onto a new line, writing to a file with the name passed in the second argument
def appendListToFile(listToWrite, fileName):
    with open(fileName, 'a') as file:
        for number in listToWrite:
            file.write('%s ' % number)
        file.write('\n')


# Open the data.text file, convert the list created from each line into a list of integers, then append the result of
# insertion sort into insert.txt
def main():
    text = openFile('data.txt')
    for line in text:
        toSort = line.split()
        del toSort[0]
        toSort = list(map(int, toSort))
        appendListToFile(insertionSort(toSort), 'insert.txt')


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
