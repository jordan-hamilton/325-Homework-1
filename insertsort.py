#!/usr/bin/env python3


def openFile(fileName):
    with open(fileName, 'r') as file:
        contents = file.readlines()
    return contents


def appendListToFile(listToWrite, fileName):
    with open(fileName, 'a') as file:
        for number in listToWrite:
            file.write('%s ' % number)
        file.write('\n')


def main():
    text = openFile('data.txt')
    for line in text:
        toSort = line.split()
        del toSort[0]
        toSort = list(map(int, toSort))
        appendListToFile(insertionSort(toSort), 'insert.txt')


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
