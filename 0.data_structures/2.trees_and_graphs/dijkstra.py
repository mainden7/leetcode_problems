def make_graph():
    graph = {
        1: [(2, 7), (3, 9), (6, 14)],
        2: [(3, 10), (4, 15)],
        3: [(6, 2), (4, 11)],
        4: [(5, 6)],
        6: [(5, 9)],
    }
    return graph


def dijkstra(graph):
    res = {1: 0}
    vertex = 1
    queue = [vertex]
    while queue:
        V = queue.pop(0)
        neighs = graph.get(V, [])
        for (i, d) in neighs:
            res[i] = min(d + res[V], res.get(i, float("inf")))
            queue.append(i)
    return res


if __name__ == "__main__":
    g = make_graph()
    dijkstra(g)
