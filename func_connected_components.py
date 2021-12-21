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

    adj_matrix = dict()  # Initialise dict, that will be a matrix

    for node1, node2 in graph[1:]:  # iterate over the edges of graph

        if node1 not in adj_matrix:  # if some nodes not in dict yet,
            # add them as keys, otherwise add add new node to elements
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

    # initialise stack and set of visited nodes
    stack, visited = [start], set()

    while stack:  # run till stack is non-emty
        node = stack.pop()
        if node in visited:  # if node was already visited, get another
            continue

        for neighbour in graph[node]:  # add all node's neighbours to the stack
            stack.append(neighbour)

        visited.add(node)  # add node to set of visited nodes

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

    # create adjacency matrix from list of edges
    matrix_graph = create_adj_matrix(graph)
    # create set of nodes that have not been added to any connected component
    nodesleft = set(matrix_graph.keys())
    # initialise empty list of connected components
    components = []

    # run till left nodes that have not been assigned a connected component
    while nodesleft:
        # find connected component in the graph
        con_component = dfs(matrix_graph, nodesleft.pop())
        # remove all nodes that are in a component from nodesleft
        nodesleft.difference_update(con_component)
        # add connected component to list of connected components
        components.append(list(con_component))

    return components
