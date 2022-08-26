def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    cs = 0

    for index in range(len(array)):
        if index + 1 > len(array) - 1:
            break
        cn = array[index]
        rightIndex = len(array) - 1
        leftIndex = index + 1
        left = array[leftIndex]
        right = array[rightIndex]

        while True:
            cs = cn + left + right

            if left >= right:
                break

            if cs < targetSum:
                leftIndex += 1
                left = array[leftIndex]

            if cs > targetSum:
                rightIndex -= 1
                right = array[rightIndex]

            if cs == targetSum:
                result.append([cn, left, right])
                leftIndex += 1
                rightIndex -= 1
                left = array[leftIndex]
                right = array[rightIndex]
    return result
                


# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum = 18

threeNumberSum(array, targetSum)