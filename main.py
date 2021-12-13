"""
module documentation here
"""

import csv


def read_graph(path: str) -> list:
    """Return a graph, read from file,
    as a set of tuples. Each tuple
    represents an edge.

    Args:
        path (str): Path to csv file with graph

    Returns:
        set: Graph, read from file
    """
    list_of_graphs = []
    with open(path, 'r') as r_file:
        file_reader = csv.reader(r_file, delimiter="\n")
        for line in file_reader:
            apexes = line[0].split()
            list_of_graphs.append((int(apexes[0]), int(apexes[1])))
    return list_of_graphs


def write_graph(path: str, graph: list) -> None:
    """Writes graph represented as
    set of tuples, where tuple is an edge,
    in a csv file.

    Args:
        path (str): Path to csv file
        graph (set): Graph, represented by set
    """

    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter=' ')
        for edge in graph:
            writer.writerow(edge)


def connected_components():
    """
    Documentation here
    """
    pass


def strongly_connected_components():
    """
    Documentation here
    """
    pass


def connection_points():
    """
    Documentation here
    """
    pass


def bridges():
    """
    Documentation here
    """
    pass


if __name__ == "__main__":
    pass
