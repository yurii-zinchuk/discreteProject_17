"""
Documentation
"""
import main
import sys
sys.setrecursionlimit(1500)

def find_SCC(graph):
    value = 0
    stackk = []
    low = {}
    ids = [-1 for _ in range(len(graph) - 1)]
    bool_stack = [False for _ in range(len(graph) - 1)]

    matrix_graph = main.create_adj_matrix(graph[1:])


    def dfs(at, SCC=0, j=1):
        stackk.append(at)
        bool_stack[at] = True
        low[at] = ids[at] = j

        for to in matrix_graph[at]:
            if ids[to] == -1:
                dfs(to, SCC, j+1)
            if bool_stack[to]:
                low[at] = min(low[at], low[to])

        if ids[at] == low[at]:
            for node in stackk:
                stackk.pop()

                bool_stack[node] = False
                low[node] = ids[at]
                if node == at:
                    break
            return 1





    print(matrix_graph)
    for i in range(1, len(matrix_graph)):
        dfs(i)
    return low








if __name__ == "__main__":
    graph = main.read_graph("graphs/graph_100000_4999_1.csv")
    print(find_SCC(graph[1:]))