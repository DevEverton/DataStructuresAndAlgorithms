def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=True)
    blueShirtSpeeds.sort()
    maximum = 0
    minimun = 0
    size = len(redShirtSpeeds)
    for i in range(size):
    	if redShirtSpeeds[i] > blueShirtSpeeds[i]:
    		maximum += redShirtSpeeds[i]
    	else:
    		maximum += blueShirtSpeeds[i]

    	if redShirtSpeeds[i] > blueShirtSpeeds[size-i-1]:
    		minimun += redShirtSpeeds[i] 
    	else:
    		minimun += blueShirtSpeeds[size-i-1]
    return maximum if fastest else minimun




reds = [5, 5, 3, 9, 2]
blues = [3, 6, 7, 2, 1]

print(tandemBicycle(reds,blues,False))


