from collections import deque
from node import Node
import sys


class BST:

    def insert(self, root: Node, data: int) -> Node:
        if root is None:
            root = Node(data)

        elif data <= root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root
    # -----------------------------------------------------------------------

    def delete(self, root: Node, data: int) -> Node:
        if root is None:
            return

        elif data < root.data:
            self.delete(root.left, data)

        elif data > root.data:
            self.delete(root.right, data)

        # node with that value was founded
        else:
            if root.right is None and root.left is None:
                root = None

            elif root.left is None:
                root = root.right

            elif root.right is None:
                root = root.left

            # 2 children
            else:
                temp = self.min(root.right)
                root.data = temp
                root.right = self.delete(root.right, temp)

            return root

    # -----------------------------------------------------------------------

    def isInBST(self, root, data: int) -> bool:
        if root is None:
            return False

        if root.data == data:
            return True

        if data <= root.data:
            return self.isInBST(root.left, data)

        if data > root.data:
            return self.isInBST(root.right, data)
    # -----------------------------------------------------------------------

    def min(self, root: Node) -> int:
        if root is None:
            print("No elements in tree")
            return

        if root.left is None:
            return root.data

        else:
            return self.min(root.left)
    # -----------------------------------------------------------------------

    def max(self, root: Node) -> int:
        if root is None:
            print("No elements in tree")

        if root.right is None:
            return root.data

        else:
            return self.max(root.right)
    # -----------------------------------------------------------------------

    def height(self, root) -> int:
        if root is None:
            return -1

        return max(self.height(root.left), self.height(root.right)) + 1
    # -----------------------------------------------------------------------

    def isBst(self, root) -> bool:

        return self.isBstUtil(root, -sys.maxsize, sys.maxsize)

    def isBstUtil(self, root, minVal, maxVal):
        if root is None:
            return True

        if (root.data > minVal and root.data < maxVal and
           self.isBstUtil(root.left, minVal, root.data) and
           self.isBstUtil(root.right, root.data, maxVal)):
            return True

        return False
    # -----------------------------------------------------------------------

    def preOrderPrint(self, root) -> None:
        if root is None:
            return

        print(root.data)
        self.preOrderPrint(root.left)
        self.preOrderPrint(root.right)
    # -----------------------------------------------------------------------

    def levelOrder(self, root) -> None:
        if root is None:
            return

        queue = deque()
        queue.append(root)

        while(len(queue)):
            temp = queue[0]
            print(temp.data)

            if(temp.left is not None):
                queue.append(temp.left)
            if(temp.right is not None):
                queue.append(temp.right)

            queue.popleft()
    # -----------------------------------------------------------------------

    def inOrder(self, root) -> None:
        if root is None:
            return

        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)
    # -----------------------------------------------------------------------

    def treeToSortedArray(self, root, arr: list) -> None:
        if root is None:
            return

        self.treeToSortedArray(root.left, arr)
        arr.append(root.data)
        self.treeToSortedArray(root.right, arr)
    # -----------------------------------------------------------------------

    def find(self, root: Node, data: int) -> Node:
        if root is None:
            return

        if root.data == data:
            return root

        if data < root.data:
            return self.find(root.left, data)

        if data > root.data:
            return self.find(root.right, data)
    # -----------------------------------------------------------------------

    def getSuccesor(self, root: Node, data: int) -> int:
        current = self.find(root, data)

        if current is None:
            return

        elif current.right:
            # if node has right child return smallest element from right subtree
            return self.min(current.right)

        else:
            successor = None
            ancestor = root

            while(ancestor != current):
                if(current.data < ancestor.data):
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right

            return successor.data

    # -----------------------------------------------------------------------
