"""
Documentation
"""
import main
import sys
sys.setrecursionlimit(1500)

def create_Dadj_matrix(graph: list) -> dict:
    """Return adjacency matrix of a graph,
    given the list of it's edges.

    Args:
        graph (set): Graph as a list of edges

    Returns:
        dict: Adjacency matrix
    """

    adj_matrix = dict()
    for node1, node2 in graph:
        if node1 not in adj_matrix:
            adj_matrix[node1] = {node2}
        else:
            adj_matrix[node1].add(node2)
    return adj_matrix



def find_SCC(graph):
    stackk = []
    low = {}
    matrix_graph = create_Dadj_matrix(graph[1:])
    print(matrix_graph)
    ids = {key: -1 for key in list(matrix_graph.keys())}
    bool_stack = {key: False for key in list(matrix_graph.keys())}



    def dfs(at):
        stackk.append(at)
        bool_stack[at] = True
        low[at] = ids[at] = len(low) + 1

        for to in matrix_graph[at]:
            if ids[to] == -1:
                dfs(to)
            if bool_stack[to]:
                low[at] = min(low[at], low[to])

        w = -1  # To store stack extracted vertices
        if ids[at] == low[at]:
            while w != at:
                w = stackk.pop()
                yield w
                bool_stack[w] = False

            print("")

    for i in list(matrix_graph.keys()):
        print(dfs(i).__repr__())
    return low








if __name__ == "__main__":
    graph = main.read_graph("graphs/test2.csv")
    print(find_SCC(graph))
