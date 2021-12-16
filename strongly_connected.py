"""
This is script for strongly connected component search function.
"""
import sys
sys.setrecursionlimit(1000000)


def create_dadj_matrix(graph: list) -> dict:
    """Return adjacency matrix of a DIRECTED graph,
    given the list of it's edges.

    Args:
        graph (set): Directed graph as a list of edges, here a list of (int, int) tuples.

    Returns:
        dict: Adjacency matrix of directed graph
    """
    adj_matrix = dict()
    for node1, node2 in graph:
        if node1 not in adj_matrix:
            adj_matrix[node1] = {node2}
        else:
            adj_matrix[node1].add(node2)
    return adj_matrix


def find_SCC(graph):
    """
    Function which uses Tarjan's alogrithm to find
    strongly connected components of the given oriented graph.

    Tarjan's algo here -> https://youtu.be/wUgWX0nc4NY

    This algorithm depends on recursion, so on very large graphs
    encounters stack overflow.
    Args:
        graph (set): Directed graph as a list of edges, here a list of (int, int) tuples.
    Returns:
        list: list of all the SCC's of the graph, which are also lists.
    """
    end_result = []  # The list of all SCC's we are going to return
    stackk = []  # Stack for dfs()
    matrix_graph = create_dadj_matrix(graph[1:])
    used_nodes = set()
    ids = {key: -1 for key in list(matrix_graph.keys())}  # dict of id's we are giving to every node. -1 marks unvisited node
    low = {}  # dict of lowest possible id we are giving to every node after dfs
    bool_stack = {key: False for key in list(matrix_graph.keys())}  # bool stack (if node is visited or not)

    def dfs(at):
        """
        This is our Depth First Search function constructed for Tarjan's algo.

        Args:
            at (int): name of node we are going to work with.
        Returns:
            None.
        """
        result = []
        stackk.append(at)  # adding node to the stack
        bool_stack[at] = True
        low[at] = ids[at] = len(low) + 1  # giving it unique id

        for to in matrix_graph[at]:  # working with neighbours of node. If visited, run dfs for them.
            try:
                if ids[to] == -1:  # checking if visited
                    dfs(to)
                if bool_stack[to]:
                    low[at] = min(low[at], low[to])
            except KeyError:
                # Means we encountered a node which does not have neighbour nodes.
                # We add it to SCC list as a separate component
                if [to] not in end_result:
                    end_result.append([to])

        w = -1  # To store stack extracted vertices
        if ids[at] == low[at]:  # if dfs encountered a loop, write down SCC and delete its' nodes from stack
            while w != at:
                w = stackk.pop()
                if w not in used_nodes:
                    result.append(w)
                bool_stack[w] = False
            used_nodes.update(result)
            if len(result) > 0:
                end_result.append(sorted(result))

    for i in list(matrix_graph.keys()):
        dfs(i)
    return end_result
