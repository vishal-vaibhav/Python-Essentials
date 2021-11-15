"""
Program to find out the height/depth of binary tree
Formulle: Height = (1+no of edges logest from root to leaf)
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height_tree(A):
    if(A == None):# checks of there are node present
        return 0
    else: #actuallogic 
        ldepth = height_tree(A.left)
        rdepth = height_tree(A.right)

        if(ldepth > rdepth):
            return (1 +ldepth)
        else:
            return(1+rdepth)

#defining Nodes of binary tree:
root = Node(1)
root.left = Node(2)
root.right  = Node(3)
root.left.left = Node(4)
root.left.right  = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)


print(height_tree(root)) # print the output (i.e., 4)

