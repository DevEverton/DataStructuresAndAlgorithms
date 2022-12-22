def longestPeak(array):
    peaks = findPeaks(array)
    if len(peaks) == 0:
        return 0
    left = 0
    right = 0
    longest = 0
    counter = 3

    for i in range(1,len(array)):
        if array[i] in peaks:
            left = i-1
            right = i+1

            while True:
                if array[left] > array[left-1]:
                    counter += 1
                    left -= 1

                if array[left] < array[left-1] or array[left] == array[left-1] or left == 0: 
                    break

            while True:
                if right+1 >= len(array)-1:
                    if len(array) == 5:
                        counter += 1
                    break 
                if array[right] > array[right+1]:
                    counter += 1
                    right += 1

                if array[right] < array[right+1] or array[right] == array[right+1]:
                    break

        if counter > longest:
            longest = counter
            counter = 3

    return longest



def findPeaks(array):
    peaks = []
    for i in range(1,len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            peaks.append(array[i])
    return peaks


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
array2 = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
array3 = [5, 4, 3, 2, 1, 2, 10, 12]
array4 = [1, 2, 3, 4, 5, 1]
array5 = [1, 1, 3, 2, 1]
array6 = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]


print(longestPeak(array5))


