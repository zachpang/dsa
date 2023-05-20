from collections import deque


def bfs(adj_lists, start, end=None):
    """
    Perform breadth-first search.

    A tuple of 2 dictionaries is returned as the result.
    - levels_of_vertices identifies the level/distance of each vertex from the start vertex.
    - parents_of_vertices identifies the parent of each vertex. The parent is the adjacent vertex that was visited before arriving at the current vertex.
    """
    levels_of_vertices = {start: 0}
    parents_of_vertices = {start: None}

    level = 1
    processing = [start]

    while processing:
        next_processing = []

        for vertex in processing:
            for neighbor in adj_lists[vertex]:
                if neighbor in parents_of_vertices:
                    # we dual-purpose the parents_of_vertices to check if a vertex has been visited
                    continue

                levels_of_vertices[neighbor] = level
                parents_of_vertices[neighbor] = vertex
                next_processing.append(neighbor)

                if end is not None and neighbor == end:
                    return (levels_of_vertices, parents_of_vertices)

        processing = next_processing
        level += 1

    return (levels_of_vertices, parents_of_vertices)


def find_shortest_path(adj_lists, start, end):
    """Find shortest path between start vertex and end vertex."""
    (levels, parents) = bfs(adj_lists, start, end)

    current = end
    path = deque([end])

    # trace path from end to start
    while current != start:
        path.appendleft(parents[current])
        current = parents[current]

    return path
