class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_height(root):
    if root is None:
        return 0
    else:
        left_height = find_height(root.left)
        right_height = find_height(root.right)
        return max(left_height, right_height) + 1

