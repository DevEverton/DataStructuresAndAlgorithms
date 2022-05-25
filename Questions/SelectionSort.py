def selectionSort(array):
    i = 0
    indexOfSmaller = 0
    while i < len(array):
        for index in range(len(array[i:])):
            if array[i:][index] < array[i:][indexOfSmaller]:
                indexOfSmaller = index
        array[i], array[indexOfSmaller+i] = array[indexOfSmaller+i], array[i]
        i += 1
        indexOfSmaller = 0
    print(array)
        

array = [8, 5, 2, 9, 5, 6, 3]
selectionSort(array)
