
def smallestDifference(arrayOne, arrayTwo):
    smallestDiff = diffInRange(arrayOne[0], arrayTwo[0])
    smallest = (arrayOne[0], arrayTwo[0])

    arrayOne.sort()
    arrayTwo.sort()

    i = 0
    j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        print((arrayOne[i], arrayTwo[j]))
        print("Current smallest", smallestDiff)
        if diffInRange(arrayOne[i], arrayTwo[j]) < smallestDiff:
            smallest = (arrayOne[i], arrayTwo[j])
            smallestDiff = diffInRange(arrayOne[i], arrayTwo[j])

        if arrayOne[i] - arrayTwo[j]  < 0:
            if i < len(arrayOne):
                i += 1
        else:
            if j < len(arrayTwo):
                j += 1
    return smallest


def diffInRange(num1, num2):
    if num2 > num1:
        return len(range(num1, num2))
    else:
        return len(range(num2, num1))


# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# arrayOne = [-1, 5, 10, 20, 3]
# arrayTwo = [26, 134, 135, 15, 17]
# [-1,3,5,10,20]
# [15,17,26,134,135]

arrayOne = [10, 0, 20, 25, 2200]
arrayTwo = [1005, 1006, 1014, 1032, 1031]
# [0, 10, 20, 25, 2200]
# [1005, 1006, 1014, 1031, 1032]

print(smallestDifference(arrayOne, arrayTwo))










