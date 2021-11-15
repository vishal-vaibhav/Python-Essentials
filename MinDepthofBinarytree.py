"""
Program to find out the minimum height/depth of binary tree
Formulle: Height = (1+no of edges longest from root to leaf)
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def min_height_binary(root):
    if(root == None):
        return 0
    else:
        ldepth = min_height_binary(root.left)
        rdepth = min_height_binary(root.right)

        if(ldepth > rdepth): # logic for getting min depth
            return (1 + rdepth)
        else:
            return(1 + ldepth)



#defining Nodes of binary tree:
root = Node(1)
root.left = Node(2)
root.right  = Node(3)
root.left.left = Node(4)
root.left.right  = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)

print(min_height_binary(root)) # print the output (i.e., 2)


