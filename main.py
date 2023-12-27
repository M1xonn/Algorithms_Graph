from arraylist import ArrayList
from graph import Graph


def parseHeader(header):
    header = header.split(" ")
    header[-1] = header[-1][0]
    return header


def parseData(data):
    pretty_matrix = ArrayList()
    shitty_matrix = data.split("\n")
    for i in range(len(shitty_matrix)):
        pretty_matrix.push(shitty_matrix[i].split(" "))

    for i in range(len(pretty_matrix)):
        for j in range(len(pretty_matrix[i])):
            pretty_matrix[i][j] = int(pretty_matrix[i][j])
    return pretty_matrix


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
