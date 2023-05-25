def directed_graph_has_cycles(vertices, adj_lists):
    """
    Checks for cycles in a graph using DFS.

    args:
    vertices -- list of Vertex objects
    adj_lists -- list of each vertex's adjacency list. Each adjacency list contains references to the adjacent Vertex objects
    """
    for vertex in vertices:
        if getattr(vertex, "visited", False):
            continue

        has_cycles = subgraph_has_cycles(vertex, adj_lists)
        if has_cycles:
            return True

    return False


def subgraph_has_cycles(start, adj_lists):
    start.visited = True
    start.processing = True

    for neighbor in adj_lists[start.name]:
        if getattr(neighbor, "processing", False):
            # cycle detected
            return True

        if getattr(neighbor, "visited", False):
            continue

        has_cycles = subgraph_has_cycles(neighbor, adj_lists)

        if has_cycles:
            return True

    start.processing = False
