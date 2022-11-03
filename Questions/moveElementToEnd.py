def moveElementToEnd(array, toMove):

    index = 0
    
    while index < len(array):
        element = array[index]
        if element == toMove:
            array.remove(element)
            array.append(element)
        index += 1

    print(array)



array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

moveElementToEnd(array, toMove)