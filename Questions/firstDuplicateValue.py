def firstDuplicateValue(array):
    dict = {}
    result = -1
    upperBound = len(array) - 1

    for i in range(0, len(array)):
        if array[i] not in dict:
            dict[array[i]] = False
        elif array[i] in dict and dict[array[i]] == True:
            pass
        else:
            if i <= upperBound:
                upperBound = i
                result = array[i]

    return result


array = [2, 1, 5, 2, 3, 3, 4]
array2 = [23, 21, 22, 5, 3, 13, 11, 16, 5, 11, 9, 14, 23, 3, 2, 2, 5, 11, 6, 11, 23, 8, 1]

print(firstDuplicateValue(array2))