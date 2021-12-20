"""
Module for functions that write and read graphs
"""


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
