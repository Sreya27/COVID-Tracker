# 2. Inorder, preorder and postorder tree traversal
class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data) 
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print("Preorder traversal sequence:")
root.preorder(root)
print("\n")
print("Postorder traversal sequence:")
root.postorder(root)
print("Inorder traversal sequence:")
root.inorder(root)

