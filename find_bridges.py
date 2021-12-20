"""
documentation
"""
import sys
sys.setrecursionlimit(5000)


def create_adj_matrix(graph: list, directed: bool = False) -> dict:
    """Return adjacency matrix of a graph,
    given the list of it's edges.

    Args:
        graph (list): Graph as a list of edges
        directed (bool): Sets if the graph is directed or not

    Returns:
        dict: Adjacency matrix
    """

    adj_matrix = dict()

    for node1, node2 in graph:
        if node1 not in adj_matrix:
            adj_matrix[node1] = {node2}
        else:
            adj_matrix[node1].add(node2)

        if not directed:
            if node2 not in adj_matrix:
                adj_matrix[node2] = {node1}
            else:
                adj_matrix[node2].add(node1)

    return adj_matrix


def _find_bridges(graph_dict, vertices, u, visited, parent, low, disc, time, bridges):
    """
    Documentation here
    """
    idx = vertices.index(u)
    visited[idx] = True
    disc[idx] = time
    low[idx] = time
    time += 1

    for ver in graph_dict[u]:
        idx_1 = vertices.index(ver)
        if visited[idx_1] is False:
            parent[idx_1] = u
            _find_bridges(graph_dict, vertices, ver, visited, parent, low, disc, time, bridges)
            low[idx] = min(low[idx], low[idx_1])
            if low[idx_1] > disc[idx]:
                bridge = (u, ver)
                bridges.append(bridge)
        elif ver != parent[idx]:
            low[idx] = min(low[idx], disc[idx_1])
    return bridges


def find_bridges(graph):
    """
    Documentation here
    """
    graph_dict = create_adj_matrix(graph)
    vertices = list(graph_dict.keys())
    vertices_num = len(graph_dict)
    bridges = []
    time = 0
    visited = [False] * vertices_num
    disc = [0] * vertices_num
    low = [0] * vertices_num
    parent = [0] * vertices_num
    for i in graph_dict:
        if visited[vertices.index(i)] is False:
            return _find_bridges(graph_dict, vertices, i, visited, parent, low, disc, time, bridges)
