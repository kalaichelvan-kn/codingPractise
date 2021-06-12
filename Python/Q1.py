#Q1 Given a k sorted array of possible different sizes. Find the mth smallest element in the final merged array formed
# by merging all the k sorted array.

from collections import deque
import bisect

def checkandInsert(element):
    if element in mergedArray:
        return True
    if len(mergedArray) == m:
        if mergedArray[m-1] > element:
            mergedArray.pop()
            bisect.insort(mergedArray, element)
            return True
        else:
            return False
    else:
        bisect.insort(mergedArray, element)
        return True
    # returns whether element is inserted or not
    pass

def findMthSmallestElement(sortedArrays):
    while len(sortedArrays) > 0:
        flag = False
        for ind, arr in enumerate(sortedArrays):
            if len(arr) != 0:
                if checkandInsert(arr.pop(0)):
                    flag = True
        print(mergedArray)
        if not any(sortedArrays) or not flag:
            break
    return mergedArray.pop()
    pass


if __name__ == '__main__':
    sortedArrays = [
        [1],
        [3, 4],
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    global m
    m = 4

    global flag

    # holds list of sorted unique elements with limit m numbers
    global mergedArray
    mergedArray = deque()

    answer = findMthSmallestElement(sortedArrays)

    print(answer)