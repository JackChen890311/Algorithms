class UF:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N
        self.count = N

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.count -= 1
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            return True # Union successful
        return False # Already in the same set

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] # 我的老爸變成我祖父
            x = self.parent[x] # 我變成我祖父繼續找
        return x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':
    N = 10
    uf = UF(N)
    merge = [(0,1), (2,3), (2,5), (6,7), (8,6), (8,9)]
    for x, y in merge:
        uf.union(x, y)
    print('Components Count:', uf.count)
    print('Parent Array:')
    print(list(range(N)))
    print(uf.parent)
    print('Parent of 2:', uf.find(2))
    print('Parent Array:')
    print(list(range(N)))
    print(uf.parent)
    print('Connected? 2, 5:', uf.is_connected(2, 5))