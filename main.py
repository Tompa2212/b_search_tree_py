from bst import BST

if __name__ == "__main__":
    tree = BST()
    root = None

    root = tree.insert(root, 5)
    tree.insert(root, 10)
    tree.insert(root, 15)
    tree.insert(root, 2)
    tree.insert(root, 3)
    tree.insert(root, 1)
    tree.insert(root, 7)

    print(tree.getSuccesor(root, 7))

    # tree.inOrder(root)

    # tree.delete(root, 10)
    # print('After deleting')

    # tree.inOrder(root)

    # print('Enter number you want to search')
    # num = int(input('> '))

    # if(tree.search(root, num)):
    #     print('True')
    # else:
    #     print('False')

    # print(f"Smallest number in tree is: {tree.min(root)}")
    # print(f"Biggest number in tree is: {tree.max(root)}")
    # print(f"Height of tree is: {tree.height(root)}")

    # arr = list()

    # tree.treeToSortedArray(root, arr)

    # print(arr)

    # print('Binary Search Tree') if tree.isBst(
    #     root) else print('Not Binary Search Tree')
