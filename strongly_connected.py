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
    j = 0


    def dfs(at, j):
        flag = False
        stackk.append(at)
        bool_stack[at] = True
        j += 1
        low[at] = ids[at] = len(low)

        for to in matrix_graph[at]:
            if ids[to] == -1:
                dfs(to, j)
            if to == at:
                flag = True
            if bool_stack[to] and not flag:
                low[at] = min(low[at], low[to])

        if ids[at] == low[at] and not flag:
            for node in stackk:
                stackk.pop()

                bool_stack[node] = False
                low[node] = ids[at]
                if node == at:
                    break
            return 1

    for i in list(matrix_graph.keys()):
        dfs(i, j)
    return low








if __name__ == "__main__":
    graph = main.read_graph("graphs/test2.csv")
    print(find_SCC(graph))
