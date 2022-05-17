def findThreeLargestNumbers(array):
    result = []
    for i in range(3):
        print(array)
        result.append(getBiggest(array))
    result.sort()
    return result


def getBiggest(array):
    biggest = -9999999
    for i in array:
        if i > biggest:
            biggest = i
    array.remove(biggest)
    return biggest


arr =  [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
findThreeLargestNumbers(arr)