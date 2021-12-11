"""
module documentation here
"""
#Commit thisсщь

def read_graph_from_file(path_file: str):
    """
    The function reads apexes of the graph from file

    """
    list_of_graphs = []
    with open(path_file, 'r') as r_file:
        file_reader = csv.reader(r_file, delimiter = "\n")
        for line in file_reader:
            apexes = line[0].split()
            list_of_graphs.append((int(apexes[0]), int(apexes[1])))
    return list_of_graphs
    # print(read_graph_from_file('graph_100_1942_0.csv'))



def write_graph_to_file(path_file: str, list_with_graphs: list):
    """
    The function writes list of tuples with apexes to the file in csv format

    """
    with open(path_file, 'w') as w_file:
        for one_tuple in list_with_graphs:
            for item in one_tuple:
                if one_tuple.index(item) == 0:
                    w_file.write(str(item) + ' ')
                else:
                    w_file.write(str(item))
            w_file.write('\n')
            # write_graph_to_file('dyskr_14.csv',read_graph_from_file('graph_100_1942_0.csv'))


def find_connected_components():
    """
    Documentation here
    """
    pass


def find_strongly_connected_components():
    """
    Documentation here
    """
    pass


def пошук_точок_сполучення():
    """
    чесно хз як назвати нормально на англ
    Documentation here
    """
    pass

aodsaoiasodisa
def find_bridges():
    """
    Documentation here
    """
    pass

