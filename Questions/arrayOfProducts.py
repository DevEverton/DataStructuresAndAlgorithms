from functools import reduce

def arrayOfProducts(array):
    result = [0 for i in range(len(array))]
    temp = 0

    for i in range(0,len(array)):
        temp = array[i]
        array[i] = 1
        result[i] = getProduct(array)
        array[i] = temp

    return result

def getProduct(array):
    return reduce(lambda x,y:x*y,array)

array = [5, 1, 4, 2]
array2 = [0,1,2,5,3]


print(arrayOfProducts(array))