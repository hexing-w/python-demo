class Node(object):
    def __init__(self, key, value):
        self.lchild = None
        self.rchild = None
        self.key = key
        self.value = value


class BST(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        self.__insert(self.root, key, value)

    def _insert(self, node, key, value):
        """迭代方法实现"""
        pass

    def __insert(self, node, key, value):
        """递归实现"""
        if not node:
            _node = Node(key, value)
            return _node
        if node.key == key:
            node.value = value
            return node
        if node.key > key:
            node.lchild = self.__insert(node.lchild, key, value)
        else:
            node.rchild = self.__insert(node.rchild, key, value)
        return node


    def preorder(self,tree):
        "根左右遍历"
        if not tree:
            return tree
        if hasattr(tree,'root'):
            print(tree.root.key)
            self.preorder(tree.root.lchild)
            self.preorder(tree.root.rchild)
        else:
            print(tree.key)
            self.preorder(tree.lchild)
            self.preorder(tree.rchild)


if __name__ == "__main__":
    bst = BST()
    bst.insert(10, 'a')
    bst.insert(3, 'b')
    bst.insert(11, 'c')
    bst.insert(5, 'c')

    print(bst)
    l = BST()
    l.preorder(bst)
