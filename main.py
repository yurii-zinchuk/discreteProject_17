"""
This module contains functions to work with graphs.
Functions are able to analyse graphs' connected components,
strongly connected components, briges and connection points.
"""
import func_strongly_connected
import func_find_bridges
import func_cut_vertices


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


def find_bridgess(graph):
    """
    Documentation here
    >>> find_bridgess([("NUMBER OF NODES", "NUMBER OF VERTEXES"), (0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (5, 1), (2, 6), (6, 7), (7, 8), (6, 8)])
    [(3, 4), (2, 6), (0, 1)]
    >>> find_bridgess([("NUMBER OF NODES", "NUMBER OF VERTEXES"),(1, 2), (2, 3), (3, 1), (2, 4), (4, 5), (5, 6), (4, 6)])
    [(2, 4)]
    """
    return func_find_bridges.find_bridges(graph)
