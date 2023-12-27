from timsort import TimSort
from disjointset import DisJointSet
from arraylist import ArrayList
from hashmap import fill


class Graph:
    def __init__(self, matrix=None, vertices=None):
        self.matrix = matrix
        self.vertices = vertices
        self.list = self.fromAdjToList()
        self.incident = self.fromAdjToIncident()

    def fromAdjToList(self):
        edges = ArrayList()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    edge = [self.vertices[i], self.vertices[j], self.matrix[i][j]]
                    edges.push(edge)
        return edges

    def fromAdjToIncident(self):
        incid = ArrayList(fill(0, len(self.vertices)))
        edge = 0
        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    incid.push(fill(0, len(self.vertices)))
                    incid[edge][j] = self.matrix[i][j]
                    edge += 1
        return incid[:-1]

    def Kruskal(self):
        path = ArrayList()
        path_len = 0
        edges = TimSort(self.list, 2)
        set = DisJointSet()
        for edge in edges:
            set.create(edge[0])
            set.create(edge[1])

        for edge in edges:
            if set.rank[edge[0]] == len(self.vertices) - 1 or set.rank[edge[1]] == len(self.vertices) - 1:
                break
            if set.get(edge[0]) != set.get(edge[1]):
                node = [edge[0], edge[1]]
                path.push(node)
                set.union(edge[0], edge[1])
                path_len += edge[2]
        return path, path_len

    def dfs(self, curr):
        visited = fill(False, len(self.vertices))
        stack = ArrayList(curr)
        visited[curr] = True
        while stack:
            vis = stack[0]
            stack.pop()
            print(self.vertices[vis])
            for i in range(len(self.vertices)):
                if self.matrix[vis][i] != 0 and not visited[i]:
                    stack.push(i)
                    visited[i] = True

    def bfs(self, curr):
        visited = fill(False, len(self.vertices))
        queue = ArrayList(curr)
        visited[curr] = True
        while queue:
            vis = queue[0]
            queue.pop_front()
            print(self.vertices[vis])
            for i in range(len(self.vertices)):
                if self.matrix[vis][i] != 0 and not visited[i]:
                    queue.push(i)
                    visited[i] = True
