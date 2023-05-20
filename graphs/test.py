from bfs import bfs


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


# bfs test cases
def test_bfs_directed_graph():
    start = vertices[0]

    # when
    (levels, parents) = bfs(directed_adj_lists, start)

    # then
    assert levels == {0: 0, 1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2}
    assert parents == {0: None, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 3} or {
        0: None,
        1: 0,
        2: 0,
        3: 0,
        4: 3,
        5: 1,
        6: 2,
        7: 3,
    }


def test_bfs_directed_graph_given_end():
    start = vertices[0]
    end = vertices[6]

    # when
    (levels, parents) = bfs(directed_adj_lists, start, end)

    # then
    assert levels == {0: 0, 1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2}
    assert parents == {0: None, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2} or {
        0: None,
        1: 0,
        2: 0,
        3: 0,
        4: 3,
        5: 1,
        6: 2,
    }


def test_bfs_undirected_graph():
    start = vertices[0]

    # when
    (levels, parents) = bfs(undirected_adj_lists, start)

    # then
    assert levels == {0: 0, 1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2}
    assert parents == {0: None, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 3} or {
        0: None,
        1: 0,
        2: 0,
        3: 0,
        4: 3,
        5: 1,
        6: 2,
        7: 3,
    }


if __name__ == "__main__":
    test_bfs_directed_graph()
    test_bfs_directed_graph_given_end()
    test_bfs_undirected_graph()
