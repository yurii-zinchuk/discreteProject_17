"""
Documentation
"""
import main
import sys
sys.setrecursionlimit(100000)


def create_dadj_matrix(graph: list) -> dict:
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
    end_result = []
    used_nodes = set()
    stackk = []
    low = {}
    matrix_graph = create_dadj_matrix(graph[1:])
    ids = {key: -1 for key in list(matrix_graph.keys())}
    bool_stack = {key: False for key in list(matrix_graph.keys())}

    def dfs(at):
        result = []
        stackk.append(at)
        bool_stack[at] = True
        low[at] = ids[at] = len(low) + 1

        for to in matrix_graph[at]:
            try:
                if ids[to] == -1:
                    dfs(to)
                if bool_stack[to]:
                    low[at] = min(low[at], low[to])
            except KeyError:
                # Means we encountered a node which does not have neighbour nodes.
                # We add it to SCC list as a separate component
                if [to] not in end_result:
                    end_result.append([to])

        w = -1  # To store stack extracted vertices
        if ids[at] == low[at]:
            while w != at:
                w = stackk.pop()
                if w not in used_nodes:
                    result.append(w)
                bool_stack[w] = False
            used_nodes.update(result)
            if len(result) > 0:
                end_result.append(result)

    for i in list(matrix_graph.keys()):
        dfs(i)
    return end_result


if __name__ == "__main__":
    graph = main.read_graph("graphs/test4.csv")
    print(find_SCC(graph))
