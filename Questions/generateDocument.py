# def generateDocument(characters, document):
#     listChar = list(characters)
    
#     for char in document:
#         if char in listChar:
#             listChar.remove(char)
#         else:
#             return False
#     return True


def generateDocument(characters, document):

    charsDict = {}

    for char in characters:
        if char in charsDict:
            charsDict[char] += 1
        else:
            charsDict[char] = 1
    
    for char in document:
        print(characters.count(characters))

        if char in charsDict:
            if charsDict[char] == 0:
                return False
            else:
                charsDict[char] -= 1
        else:
            return False

    return True



characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))