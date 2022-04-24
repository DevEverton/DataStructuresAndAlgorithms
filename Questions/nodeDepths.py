def nodeDepths(root):
    depthArr = []
    nodeDepthsHelper(root, depthArr, 0)
    if len(depthArr) == 0:
        return 0
    return sum(depthArr)



def nodeDepthsHelper(node, depthArr, currentDepth):
    if node is None:
        return
    
    depthArr.append(currentDepth)

    if node.left is None and node.right is None:
        return
    else:
        currentDepth += 1
        nodeDepthsHelper(node.left, depthArr, currentDepth)
        nodeDepthsHelper(node.right, depthArr, currentDepth)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BinaryTree(10)
# root.left = 5
# root.right = 6

nodeDepths(root)
