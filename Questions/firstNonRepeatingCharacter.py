def firstNonRepeatingCharacter(string):
    charsDict = {}
    index = 0

    for char in string:
        if char in charsDict:
            charsDict[char] += 1
        else:
            charsDict[char] = 1
    
    for char in string:
        if charsDict[char] == 1:
            return index
        else:
            index += 1
    return -1





string = "abcdcaf"

print(firstNonRepeatingCharacter(string))