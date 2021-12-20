"""
This module has funcrions required to find connected components
"""


def create_adj_matrix(graph: list) -> dict:
    """Return adjacency matrix of a graph,
    given the list of it's edges.

    Args:
        graph (list): Graph as a list of edges

    Returns:
        dict: Adjacency matrix
    """

    adj_matrix = dict()

    for node1, node2 in graph[1:]:
        if node1 not in adj_matrix:
            adj_matrix[node1] = {node2}
        else:
            adj_matrix[node1].add(node2)

        if node2 not in adj_matrix:
            adj_matrix[node2] = {node1}
        else:
            adj_matrix[node2].add(node1)

    return adj_matrix


def dfs(graph: dict, start: int) -> set:
    """Return a sequence of nodes after dfs.

    Args:
        graph (dict): Adjacency matrix of a graph
        start (int): Starting node

    Returns:
        set: Nodes visited after dfs
    """

    stack, visited = [start], set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        for neighbour in graph[node]:
            stack.append(neighbour)

        visited.add(node)

    return visited


def connected_components(graph: list) -> list:
    """Return a list containing conncected components.
    Connected component is identified by the node with least number
    that belongs to a the component.

    Args:
        graph (list): Graph as a list of edges

    Returns:
        list: Connected components
    """

    matrix_graph = create_adj_matrix(graph)
    nodesleft = set(matrix_graph.keys())
    components = []

    while nodesleft:
        con_component = dfs(matrix_graph, nodesleft.pop())
        nodesleft.difference_update(con_component)
        components.append(list(con_component))

    return components
