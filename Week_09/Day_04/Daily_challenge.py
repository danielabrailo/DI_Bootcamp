class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def set_value(self, value):
        self.value = value

    def add_node(self, node):
        if node.value < self.value:
            if not self.left:
                self.left = node
        else:
            if not self.right:
                self.right = node

    def search(self, value):
        if self.value == value:
            print(f"The value {value} was found in {self}")
            return
        elif self.value > value:
            self.left.search(value)
        elif self.value < value:
            self.right.search(value)
        else:
            print("Value not found")


root = Node(8)
print(root)
node_10 = Node(10)
print(node_10)
root.add_node(node_10)
node_3 = Node(3)
print(node_3)
root.add_node(node_3)

root.search(10)
