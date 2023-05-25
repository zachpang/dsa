from vertex import Vertex
from cycle_detection import directed_graph_has_cycles

vertices = [
    Vertex(0),
    Vertex(1),
    Vertex(2),
    Vertex(3),
    Vertex(4),
    Vertex(5),
]


def test_directed_graph_has_cycles():
    graph_with_cycles = [
        [vertices[1]],
        [vertices[3], vertices[4], vertices[5]],
        [],
        [vertices[2]],
        [vertices[3], vertices[5]],
        [vertices[0]],
    ]

    assert directed_graph_has_cycles(vertices, graph_with_cycles)

    graph_without_cycles = [
        [vertices[1]],
        [vertices[3], vertices[4], vertices[5]],
        [],
        [vertices[2]],
        [vertices[3], vertices[5]],
        [],
    ]

    assert not directed_graph_has_cycles(vertices, graph_without_cycles)


if __name__ == "__main__":
    test_directed_graph_has_cycles()
