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
        appendListToFile(mergeSort(toSort), 'merge.txt')


def mergeSort(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        left = numbers[:len(numbers) // 2]
        right = numbers[len(numbers) // 2:]

        return merge(mergeSort(left), mergeSort(right))


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
