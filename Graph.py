from collections import deque

def dfsM(matrix, s):
    S = [s]
    visited = {s,}
    while S:
        curr = S.pop()
        print(curr, end=' -> ')
        for i in range(N):
            if i not in visited and matrix[curr][i]:
                S.append(i)
                visited.add(i)

def bfsM(matrix, s):
    Q = deque([s])
    visited = {s,}
    while Q:
        curr = Q.popleft()
        print(curr, end=' -> ')
        for i in range(N):
            if i not in visited and matrix[curr][i]:
                Q.append(i)
                visited.add(i)

def dfsA(adjacent, s):
    S = [s]
    visited = {s,}
    while S:
        curr = S.pop()
        print(curr, end=' -> ')
        for i in adjacent[curr]:
            if i not in visited:
                S.append(i)
                visited.add(i)

def bfsA(adjacent, s):
    Q = deque([s])
    visited = {s,}
    while Q:
        curr = Q.popleft()
        print(curr, end=' -> ')
        for i in adjacent[curr]:
            if i not in visited:
                Q.append(i)
                visited.add(i)

if __name__ == '__main__':
    N = 10
    matrix = [[0] * N for i in range(N)]
    adjacent = [[] * N for i in range(N)]
    for i in range(N):
        matrix[i][i] = 1
    edges = [(0,1),(1,3),(0,2),(2,4),(0,5),(3,7),(7,8),(3,9),(9,6)]
    '''
    0 - 1 - 3 - 7 - 8
              - 9 - 6
      - 2 - 4
      - 5
    '''
    for e in edges:
        matrix[e[0]][e[1]] = 1
        matrix[e[1]][e[0]] = 1
        adjacent[e[0]].append(e[1])
        adjacent[e[1]].append(e[0])

    print('DFS: ')
    dfsM(matrix,0)
    print('\nBFS: ')
    bfsM(matrix,0)

    print('\nDFS: ')
    dfsA(adjacent,0)
    print('\nBFS: ')
    bfsA(adjacent,0)


    

    


