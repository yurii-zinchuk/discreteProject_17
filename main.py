"""
This module contains functions to work with graphs.
Functions are able to analyse graphs' connected components,
strongly connected components, briges and connection points.
"""
import strongly_connected
import csv


def read_graph(path: str) -> list:
    """Return a graph, read from file,
    as a list of tuples. Each tuple
    represents an edge.

    Args:
        path (str): Path to csv file with graph

    Returns:
        list: Graph, read from file
    """

    graph = list()

    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for line in reader:
            graph.append((int(line[0]), int(line[1])))

    return graph
  
  
def write_graph(path: str, graph: list) -> None:
    """Writes graph represented as
    list of tuples, where tuple is an edge,
    in a csv file.

    Args:
        path (str): Path to csv file
        graph (list): Graph, represented by list
    """

    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter=' ')
        for edge in graph:
            writer.writerow(edge)


def create_adj_matrix(graph: list, directed: bool=False) -> dict:
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
    """Return a list containing connected components.
    Connected component is identified by the node with least number
    that belongs to a the component.

    Args:
        graph (list): Graph as a list of edges

    Returns:
        list: Connected components
    """

    matrix_graph = create_adj_matrix(graph[1:])
    nodesleft = set(matrix_graph.keys())
    components = []

    while nodesleft:
        con_component = dfs(matrix_graph, nodesleft.pop())
        nodesleft.difference_update(con_component)
        components.append(list(con_component))

    return components


def strongly_connected_components(graph):
    """
    Documentation here
    """
    strongly_connected.find_SCC(graph)


def dfs_tree(graph:dict, start:int) -> dict:
    """
    Beautiful, but useless

    Returns an adjacency matrix for a DFS Spanning tree from the given graph

    Args:
        graph (dict): Adjacency matrix of a graph
        start (int): Starting node

    Returns:
        dict: Adjacency matrix of a DFS spanning tree of the given graph
    """

    stack, dfs_tree, visited = [start], {}, set()

    while stack:
        node = stack[-1]
        visited.add(node)

        for neighbour in sorted(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                break
        else:
            stack.pop()
            continue

        if len(stack) > 1:
            # print(stack[-2], stack[-1])
            if stack[-2] not in dfs_tree.keys():
                dfs_tree[stack[-2]] = {stack[-1]}
            else:
                dfs_tree[stack[-2]] |= {stack[-1]}
            if stack[-1] not in dfs_tree.keys():
                dfs_tree[stack[-1]] = {stack[-2]}
            else:
                dfs_tree[stack[-1]] |= {stack[-2]}

    return dfs_tree


def cut_vertices(graph: dict):
    """
    A function that finds cut vertices in O(n+m)

    Args:
        graph (dict): Adjacency matrix of a graph

    Returns:
        list: numbers of points, whose removal disconnects graph
    """

    def cut_vertices_dfs(vertex: int, root, d, h, used, order, graph: dict, cut_v):
        """
        Helper function for cut_vertices
        """

        used[vertex] = 1
        d[vertex] = h[vertex] = order
        order += 1
        children = 0

        for u in graph[vertex]:
            if u == root:
                continue
            elif used[u]:
                # коли ребро зворотнє
                h[vertex] = min(h[vertex], d[u])
            else:
                # коли ребро пряме
                cut_vertices_dfs(u, vertex, d, h, used, order, graph, cut_v)
                h[vertex] = min(h[vertex], h[u])
                children += 1
                if h[u] >= d[vertex] and root != -1:
                    cut_v[vertex] = 1

        # спеціальний випадок, якщо вершина є коренем (якщо root == -1)
        if root == -1 and children > 1:
            cut_v[vertex] = 1


    n = len(graph.keys()) + 1
    used, d, h, cut_v = [0] * n, [0] * n, [0] * n, [0] * n
    for i in range(1,n):
        if used[i] == 0:
            cut_vertices_dfs(i, -1, d, h, used, 1, graph, cut_v)

    cut_v_names = []
    for i in range(n):
        if cut_v[i]:
            cut_v_names.append(i)

    return cut_v_names


def bridges():
    """
    Documentation here
    """
    pass


if __name__ == "__main__":
    my_graph = read_graph('graphs/graph_100_1942_0.csv')
    my_simple_graph = read_graph('graphs/simple_test.csv')
    print(cut_vertices(create_adj_matrix(my_simple_graph[1:])))

