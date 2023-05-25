class CycleDetectedError(Exception):
    pass


def topological_sort_dfs(vertices, adj_lists):
    visited = [False] * len(vertices)
    processing = [False] * len(vertices)

    result_stack = []

    for vertex in vertices:
        if visited[vertex.name]:
            continue

        dfs(vertex, adj_lists, visited, processing, result_stack)

    result_stack.reverse()

    return result_stack


def dfs(start, adj_lists, visited, processing, result_stack):
    visited[start.name] = True
    processing[start.name] = True

    for neighbor in adj_lists[start.name]:
        if processing[neighbor.name]:
            raise CycleDetectedError(f"backedge: {start} -> {neighbor}")

        if visited[neighbor.name]:
            continue

        dfs(neighbor, adj_lists, visited, processing, result_stack)

    processing[start.name] = False
    result_stack.append(start)


def topological_sort_kahn(vertices, adj_lists):
    # TODO: topological sort Kahn's algorithm
    pass
