from hashmap import HashMap


class DisJointSet:
    def __init__(self):
        self.parent = HashMap(50)
        self.rank = HashMap(50)

    def create(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def get(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.get(self.parent[node])
        return self.parent[node]

    def union(self, node_1, node_2):
        parent_1 = self.get(node_1)
        parent_2 = self.get(node_2)

        if parent_1 != parent_2:
            if self.rank[parent_1] > self.rank[parent_2]:
                self.parent[parent_2] = self.parent[parent_1]
                self.rank[parent_1] += 1
            else:
                self.parent[parent_1] = self.parent[parent_2]
                self.rank[parent_2] += 1

