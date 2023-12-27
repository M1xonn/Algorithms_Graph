from arraylist import ArrayList
from graph import Graph


def parseHeader(header):
    header = header.split(" ")
    header[-1] = header[-1][0]
    return header


def parseData(data):
    matrix = ArrayList()
    matrix_data = data.split("\n")
    for i in range(len(matrix_data)):
        matrix.push(matrix_data[i].split(" "))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    return matrix


if __name__ == '__main__':
    with open('data.txt') as file:
        header = file.readline()
        data = file.read()

    edges = parseHeader(header)
    adjacency_matrix = parseData(data)
    graph = Graph(adjacency_matrix, edges)
    path, path_len = graph.Kruskal()
    print(path)
    print(path_len)
