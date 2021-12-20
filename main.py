"""
This module contains functions to work with graphs.
Functions are able to analyse graphs' connected components,
strongly connected components, briges and connection points.
"""
import func_strongly_connected
import func_find_bridges
import func_cut_vertices
import func_connected_components
import read_write


def read(path: str) -> list:
    """Reads graph from file

    Args:
        path (str): path to the file

    Returns:
        list: graph as list of tuples
    """
    return read_write.read_graph()


def write(path: str, graph: list) -> None:
    """[summary]

    Args:
        path (str): path to file
        graph (list): graph as list of tuples
    """
    return read_write.write_graph(path, graph)


def strongly_connected_components(graph):
    """
    Documentation here
    >>> strongly_connected_components([("NUMBER OF NODES", "NUMBER OF VERTEXES"),(0, 1), (1, 2), (2, 3), (3, 0), (2, 4), (4, 5), (5, 6), (6, 4), (6, 7)])
    [[7], [4, 5, 6], [0, 1, 2, 3]]
    >>> strongly_connected_components([("NUMBER OF NODES", "NUMBER OF VERTEXES"), (0, 2), (2, 1), (1, 0), (0, 3), (3, 4)])
    [[4], [3], [0, 1, 2]]
    """
    return func_strongly_connected.find_SCC(graph)


def cut_vertices(graph):
    """
    A function that finds cut vertices in O(n+m)

    Args:
        graph (dict): Adjacency matrix of a graph

    Returns:
        list: numbers of points, whose removal disconnects graph

    >>> cut_vertices({1: {4}, 4: {1, 2, 3}, 2: {3, 4}, 3: {2, 4, 6, 7, 8}, \
6: {3, 5, 7}, 8: {3}, 5: {6, 7}, 7: {3, 5, 6}})
    [3, 4]
    """
    return func_cut_vertices.cut_vertices(graph)


def bridges(graph):
    """
    Documentation here
    """
    return func_find_bridges.find_bridges(graph)


def connected_components(graph: list) -> list:
    """Returns connected components of undirected graph

    Args:
        graph (list): graph as list of tuples

    Returns:
        list: list of connected components
    """
    return func_connected_components.connected_components(graph)
