def bubbleSort(array):
	swapCount = 0
	while True:
		for index in range(len(array)):
			if index + 1 > len(array) - 1:
				break
			if array[index] > array[index + 1]:
				array[index], array[index + 1] = array[index + 1], array[index]
				swapCount += 1
		if swapCount == 0:
			break
		swapCount = 0
	return array
		

array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(array))