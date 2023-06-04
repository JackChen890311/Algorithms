class TreeNode:
    def __init__(self, val, left = None, right = None):
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
    
if __name__ == '__main__':
    '''
        0
        /\
        1 2
       /\
       3 5
      /
      4
    '''
    N = 6
    nodes = [TreeNode(i) for i in range(N)]
    nodes[0].setChild(nodes[1], nodes[2])
    nodes[1].setChild(nodes[3], nodes[5])
    nodes[3].setChild(nodes[4], None)

    dfs(nodes[0])
    print('')
    print(nodes[0].val, end=' -> ')
    bfs(nodes[0])