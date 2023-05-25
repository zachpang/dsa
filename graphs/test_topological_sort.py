from vertex import Vertex
from topological_sort import (
    topological_sort_dfs,
    topological_sort_kahn,
    CycleDetectedError,
)

vertices = [
    Vertex(0),
    Vertex(1),
    Vertex(2),
    Vertex(3),
    Vertex(4),
    Vertex(5),
]

graph_with_cycles = [
    [vertices[1]],
    [vertices[3], vertices[4], vertices[5]],
    [],
    [vertices[2]],
    [vertices[3], vertices[5]],
    [vertices[0]],
]


graph_without_cycles = [
    [vertices[1]],
    [vertices[3], vertices[4], vertices[5]],
    [],
    [vertices[2]],
    [vertices[3], vertices[5]],
    [],
]


def test_topological_sort_dfs():
    assert topological_sort_dfs(vertices, graph_without_cycles) == [
        vertices[0],
        vertices[1],
        vertices[4],
        vertices[5],
        vertices[3],
        vertices[2],
    ]

    try:
        topological_sort_dfs(vertices, graph_with_cycles)

        # Topological sort should fail due to cycle. Test fails.
        assert False
    except CycleDetectedError as err:
        assert str(err) == "backedge: Vertex(5) -> Vertex(0)"


if __name__ == "__main__":
    test_topological_sort_dfs()
