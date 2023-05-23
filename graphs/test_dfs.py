from dfs import dfs_recursive, dfs_all


# fixtures
# 0 1 2 3 4 5 6 7
# A B C D E F G H
vertices = [0, 1, 2, 3, 4, 5, 6, 7]


directed_adj_lists = [
    [1, 2, 3],  # Vertex 0 is connected to vertices 1, 2, and 3
    [4, 5],  # Vertex 1 is connected to vertices 4 and 5
    [6],  # Vertex 2 is connected to vertex 6
    [4, 7],  # Vertex 3 is connected to vertices 4 and 7
    [5],  # Vertex 4 is connected to vertex 5
    [6],  # Vertex 5 is connected to vertex 6
    [],  # Vertex 6 has no outgoing edges
    [],  # Vertex 7 has no outgoing edges
]


undirected_adj_lists = [
    [1, 2, 3],  # Vertex 0 is connected to vertices 1, 2, and 3
    [0, 4, 5],  # Vertex 1 is connected to vertices 0, 4, and 5
    [0, 6],  # Vertex 2 is connected to vertices 0 and 6
    [0, 7, 4],  # Vertex 3 is connected to vertices 0, 7, and 4
    [1, 3, 5],  # Vertex 4 is connected to vertices 1, 3, and 5
    [1, 4, 6],  # Vertex 5 is connected to vertices 1, 4, and 6
    [2, 5],  # Vertex 6 is connected to vertices 2 and 5
    [3],  # Vertex 7 is connected to vertex 3
]


def test_dfs_recursive_directed_graph():
    # case 1: start = 0
    start = vertices[0]
    visited = [False] * len(vertices)

    dfs_recursive(start, directed_adj_lists, visited)

    assert visited == [True] * len(vertices)

    # case 2: start = 3
    start = vertices[3]
    visited = [False] * len(vertices)

    dfs_recursive(start, directed_adj_lists, visited)

    assert visited == [False, False, False, True, True, True, True, True]


def test_dfs_all_recursive_directed_graph():
    # vertices 8 and 9 are separated from the other vertices
    separate_vertices = [8, 9]
    all_vertices = vertices + separate_vertices
    adj_lists = directed_adj_lists + [[9], []]  # 8 -> 9

    visited = [False] * len(all_vertices)

    dfs_all(all_vertices, adj_lists, visited)

    # all vertices are visited.
    assert visited == [True] * len(all_vertices)


if __name__ == "__main__":
    test_dfs_recursive_directed_graph()
    test_dfs_all_recursive_directed_graph()
