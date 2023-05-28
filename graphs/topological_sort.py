from collections import deque


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
    # we use a dictionary, as Vertex objects are hashable to be used as a key
    indegree_counts = {vertex: 0 for vertex in vertices}

    # iterate through all neighbors and tally the indegrees of each vertex. O(V+E)
    for neighbors in adj_lists:
        for neighbor in neighbors:
            indegree_counts[neighbor] += 1

    # textbook algorithm uses a queue, but a stack or set can be used as well.
    queue = deque()

    # initialize source vertices into queue
    for vertex, count in indegree_counts.items():
        if count == 0:
            queue.append(vertex)

    ordering = []

    # O(V+E) when we enqueue/dequeue each vertex, and iterate each neighbor
    while queue:
        vertex = queue.popleft()
        ordering.append(vertex)

        for neighbor in adj_lists[vertex.name]:
            indegree_counts[neighbor] -= 1

            if indegree_counts[neighbor] == 0:
                queue.append(neighbor)

    if len(ordering) != len(vertices):
        # all remaining vertices still have inbound edges in the absence of a source vertex
        # - this indicates a cycle
        raise CycleDetectedError

    return ordering
