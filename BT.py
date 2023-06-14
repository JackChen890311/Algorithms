class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def setChild(self, left, right):
        self.left = left
        self.right = right

def dfs(root):
    print(root.val, end=' -> ')
    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)

def bfs(root):
    if root.left:
        print(root.left.val, end=' -> ')
    if root.right:
        print(root.right.val, end=' -> ')
    
    if root.left:
        bfs(root.left)
    if root.right:
        bfs(root.right)
        
def preOrderTraverse(root):
    print(root.val, end=' -> ')
    if root.left:
        preOrderTraverse(root.left)
    if root.right:
        preOrderTraverse(root.right)

def inOrderTraverse(root):
    if root.left:
        inOrderTraverse(root.left)
    print(root.val, end=' -> ')
    if root.right:
        inOrderTraverse(root.right)

def postOrderTraverse(root):
    if root.left:
        postOrderTraverse(root.left)
    if root.right:
        postOrderTraverse(root.right)
    print(root.val, end=' -> ')

'''
    4
   / \
  2   6
 / \ / \
1  3 5  7

前序 (preorder): 中 -> 左 -> 右，4213657
中序 (inorder): 左 -> 中 -> 右，1234567
後序 (postorder): 左 -> 右 -> 中，1325764

注意：對二元搜尋樹 (binary search tree, BST) 做 inorder traversal 就是由小到大依序遍歷。

Source: https://shubo.io/iterative-binary-tree-traversal/
'''

if __name__ == '__main__':
    N = 8
    nodes = [TreeNode(i) for i in range(1,N)]
    nodes[3].setChild(nodes[1], nodes[5])
    nodes[1].setChild(nodes[0], nodes[2])
    nodes[5].setChild(nodes[4], nodes[6])

    print('Pre-Order Traverse: ')
    preOrderTraverse(nodes[3])
    print('\nIn-Order Traverse: ')
    inOrderTraverse(nodes[3])
    print('\nPost-Order Traverse: ')
    postOrderTraverse(nodes[3])

    print('\nDFS: ')
    dfs(nodes[3])
    print('\nBFS: ')
    print(nodes[3].val, end=' -> ')
    bfs(nodes[3])