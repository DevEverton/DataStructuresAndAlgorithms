def binarySearch(array, target):
    low = 0
    max = len(array)
    while max > low:
        mid = int((max + low -1)/2)
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            low = mid + 1
        elif target < array[mid]:
            max = mid
    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 71

print(binarySearch(array,target))