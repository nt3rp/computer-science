class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right

    def children(self):
        if self.value is None:
            return None
        
        count = 0

        if self.left:
            count += 1
        if self.right:
            count += 1

        return count

    def __repr__(self):
        left = '-'
        right = '-'
        if self.left is not None:
            left = repr(self.left)
        if self.right is not None:
            right = repr(self.right)

        return '({0}, {1}, {2})'.format(left, self.value, right)

class BinarySearchTree(Node):
    def _find(self, x, parent=None):
        if x < self.value:
            if self.left is None:
                return None, None
            return self.left._find(x, self)
        elif x > self.value:
            if self.right is None:
                return None, None
            return self.right._find(x, self)
        else:
            return self, parent
    
    def add(self, x):
        if self.value is None:
            self.value = x
            return

        if x < self.value:
            if self.left is None:
                self.left = BinarySearchTree(x)

            else:
                self.left.add(x)

        else:
            if self.right is None:
                self.right = BinarySearchTree(x)

            else:
                self.right.add(x)

    def remove(self, x):
        node, parent = self._find(x)

        if node is None:
            return False
        
        children = node.children()

        if children == 0:
            # Special Case: Root Node
            if parent is None:
                self.value = None

            else:
                if parent.left is node:
                    parent.left = None

                else:
                    parent.right = None

                del node

        elif children == 1:
            n = node.left or node.right

            # Special Case: Root Node
            if parent is None:
                self.value = n.value
                self.left = None
                self.right = None

            else:
                if parent.left is node:
                    parent.left = n

                else:
                    parent.right = n
            

        elif children == 2:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left

            node.value = successor.value
            if parent and parent.left is successor:
                parent.left = successor.right
            elif parent and parent.right is successor:
                parent.right = successor.right

        return True

