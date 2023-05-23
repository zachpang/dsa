from collections import deque


def dfs_all(vertices, adj_lists, visited):
    """
    Perform DFS on all vertices on the graph.

    DFS will be performed on all vertices, even for vertices
    belonging to disconnected subgraphs.
    """
    for vertex in vertices:
        if visited[vertex]:
            continue

        dfs_recursive(vertex, adj_lists, visited)


def dfs_recursive(vertex, adj_lists, visited):
    # process vertex
    visited[vertex] = True

    for neighbor in adj_lists[vertex]:
        if visited[neighbor]:
            continue

        dfs_recursive(neighbor, adj_lists, visited)


def dfs_all_iterative(vertices, adj_lists, visited):
    stack = deque()

    for vertex in vertices:
        if visited[vertex]:
            continue

        stack.append(vertex)
        dfs_iterative(adj_lists, visited, stack)


def dfs_iterative(adj_lists, visited, stack):
    while stack:
        vertex = stack.pop()

        # process vertex
        visited[vertex] = True

        for neighbor in adj_lists[vertex]:
            if visited[neighbor]:
                continue

            stack.append(neighbor)
