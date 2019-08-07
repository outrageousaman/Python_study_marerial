# binary search tree


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data);

    def get_min(self):
        if self.left is None:
            return self.data
        else:
            self.left_child.get_min()

    def get_max(self):
        if self.right_child is None:
            return self.data
        else:
            self.right_child.get_max()

    def traverse_inorder(self):
        if self.left_child is not None:
            self.left_child.traverse_inorder()

        print(self.data)

        if self.right_child is not None:
            self.right_child.traverse_inorder()

