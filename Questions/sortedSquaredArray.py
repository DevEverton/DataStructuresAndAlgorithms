
def sortedSquaredArray(array):
	if len(array) == 1:
		sqr = array[0]*array[0]
		return [sqr]
	else:
		if abs(array[0]) > abs(array[len(array)]):
			return sortedSquaredArray(array[1:len(array) - 1])
		else:
			return sortedSquaredArray(array[0:len(array) - 2])



arr = [1, 2, 3, 5, 6, 8, 9]
#print(sortedSquaredArray([-2,-1]))

def tournamentWinner(competitions, results):
    # Write your code here.
    pointsTable = {}
    result = 0
    winer = ""
    idx = 0
    for i in competitions:
    	if results[idx] == 1:
    		if i[0] in pointsTable:
    			pointsTable[i[0]] += 3
    		else:
    			pointsTable[i[0]] = 3

    	else:
    		if i[1] in pointsTable:
    			pointsTable[i[1]] += 3
    		else:
    			pointsTable[i[1]] = 3
    	idx += 1
    for key in pointsTable:
    	if pointsTable[key] > result:
    		result = pointsTable[key]
    		winer = key
    return winer

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]

results = [0,0,1]
#print(tournamentWinner(competitions, results))



def nonConstructibleChange(coins):
    # Write your code here.
    change = 0
    sortedCoins = coins
    sortedCoins.sort()
    
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1


coins = [5, 7, 1, 1, 2, 3, 22] 

# nonConstructibleChange([1,2,4,6,18])


def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = target - tree.value
    if target > tree.value:
        return findClosestValueInBst(tree.right, target)
    elif target < tree.value:
        return findClosestValueInBst(tree.left, target)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



tree = { "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": None, "right": None, "value": 22},
      {"id": "13", "left": None, "right": "14", "value": 13},
      {"id": "14", "left": None, "right": None, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": None, "right": None, "value": 5},
      {"id": "2", "left": "1", "right": None, "value": 2},
      {"id": "1", "left": None, "right": None, "value": 1}
    ], "root": "10"}



findClosestValueInBst(tree, 10)




