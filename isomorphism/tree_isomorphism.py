class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isIsomorphic (n1, n2):
    if (n1 == None and n2 == None):
        return True
    elif (n1 == None or n2 == None):
        return False
    elif (n1.data != n2.data):
        return False
    else:
        is_child_iso_left = isIsomorphic (n1.left, n2.left)
        is_child_iso_right = isIsomorphic (n1.right, n2.right)
        is_child_iso_flipped_left = isIsomorphic (n1.left, n2.right)
        is_child_iso_flipped_right = isIsomorphic (n1.right, n2.left)
        is_child_iso = is_child_iso_left and is_child_iso_right
        is_child_iso_flipped = is_child_iso_flipped_left and is_child_iso_flipped_right
        return is_child_iso or is_child_iso_flipped

    return False

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)

n2 = Node(1) 
n2.left = Node(3) 
n2.right = Node(2) 
n2.right.left = Node(4) 
n2.right.right = Node(5) 
n2.left.right = Node(6) 
n2.right.right.left = Node(8) 
n2.right.right.right  = Node(7) 


if isIsomorphic(n1, n2):
    print ("Yes")
else:
    print ("No")
