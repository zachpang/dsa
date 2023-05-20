def bfs(start, adj_list):
    levels_of_vertices = {start: 0}
    parents_of_vertices = {start: None}

    level = 1
    processing = [start]

    while processing:
        next_processing = []

        for vertex in processing:
            for neighbor in adj_list[vertex]:
                if neighbor in parents_of_vertices:
                    # we dual-purpose the parents_of_vertices to check if a vertex has been visited
                    continue

                levels_of_vertices[neighbor] = level
                parents_of_vertices[neighbor] = vertex
                next_processing.append(neighbor)

        processing = next_processing
        level += 1

    return (levels_of_vertices, parents_of_vertices)
