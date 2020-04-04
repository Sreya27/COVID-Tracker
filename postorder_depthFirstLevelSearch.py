#3. postorder and depth first level search
class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data) 
def levelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        level(root,i)
def level(root,level):
    if root is None:
        return
    if level==1:
        print(root.data)
    elif level>1:
        level(root.left,level-1)
        level(root.right,level-1)
def height(node):
    if node is None:
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)
    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1

root=node('A')
root.left=node('B')
root.right=node('C')
root.left.left=node('D')
root.left.right=node('E')
root.right.left=node('F')
root.right.right=node('G')
root.left.left.left=node('H')
root.left.left.right=node('I')
root.right.left.left=node('J')
root.right.left.right=node('K')

print("Level order traversal sequence:")
levelOrder(root)
print("\nPost order traversal sequence:")
root.postorder(root)

        