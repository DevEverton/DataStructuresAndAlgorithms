def classPhotos(redShirtHeights, blueShirtHeights):

	redShirtHeights.sort()
	blueShirtHeights.sort()
	counter = 0
	i = 0

	for red in redShirtHeights:
		if red < blueShirtHeights[i]:
			counter += 1
		else:
			counter -= 1
		i += 1
	
	return abs(counter) == len(redShirtHeights)



reds = [5, 8, 1, 3, 4]
blues = [6, 9, 2, 4, 5]

# [1,3,4,5,8]
# [2,4,5,6,9]

classPhotos(reds,blues)

