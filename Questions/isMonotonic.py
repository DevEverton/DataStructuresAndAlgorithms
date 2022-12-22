def isMonotonic(array):

    if len(array) <= 1:
        return True

    isIncreasing = False
    isDecreasing = False
    allEqual = False
    currNum = array[0]
    i = 1

    while i < len(array):
        if array[i] < currNum:
            isDecreasing = True
        elif array[i] > currNum:
            isIncreasing = True
        else:
            allEqual = True
        currNum = array[i]
        i += 1

    if allEqual and not isIncreasing and not isDecreasing:
        return True
    else:
        return isDecreasing ^ isIncreasing



# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]

print(isMonotonic([2,2,2,2,2,2]))
