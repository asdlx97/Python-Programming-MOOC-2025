"""
Please write a function named greatest_node(root: Node) which takes the root node of a binary tree as its argument.

The function should return the value of the node with the greatest value within the tree. The tree should be traversed recursively.

Hint: the function sum_of_nodes in the example above may come in handy.

An example of how the function should work:

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))

Sample output
11
"""

# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    values = [root.value]

    if root.left_child is not None:
        values.append(greatest_node(root.left_child))
     
    if root.right_child is not None:
        values.append(greatest_node(root.right_child))

    return max(values)

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))

"""
#Suggested solution

class Node:
    #Class is modeling single node in binary tree
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
 
def greatest_node(root: Node):
    value = root.value
 
    if root.left_child:
        left_value = greatest_node(root.left_child)
    else:
        left_value = value
 
    if root.right_child:
        right_value = greatest_node(root.right_child)
    else:
        right_value = value
 
    return max(value, left_value, right_value)
    
 
#Review
My solution results in the same output, the suggested one works a bit
differently as it collects only the root value and both the greatest on the 
left and right of it, then takes the maximum. 
"""

