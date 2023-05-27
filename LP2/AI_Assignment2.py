import heapq


class Node:
    def __init__(self, parent, position, g, h):
        self.parent = parent
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h

    # Comparison function to determine priority in the priority queue
    def __lt__(self, other):
        return self.f < other.f


def a_star(matrix, start_loc, end_loc):
    open_list = []
    closed_set = set()

    start_node = Node(None, start_loc, 0, 0)
    end_node = Node(None, end_loc, 0, 0)

    # Push the starting node to the open list with its priority
    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current = heapq.heappop(open_list)[1]
        # Add the current node's position to the closed_set
        closed_set.add(current.position)

        # Check if we have reached the goal
        if current.position == end_loc:
            path = []
            # Reconstruct the path by traversing the parent pointers
            while current:
                path.append(current.position)
                current = current.parent
            path.reverse()
            return path

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for direction in directions:
            new_position = (
                current.position[0] + direction[0], current.position[1] + direction[1])

            # Check if the neighbor is out of bounds or blocked by an obstacle
            if (
                new_position[0] < 0 or new_position[0] >= len(matrix[0]) or
                new_position[1] < 0 or new_position[1] >= len(matrix) or
                matrix[new_position[0]][new_position[1]] != 0 or
                new_position in closed_set  # Check if the new position is already in the closed set
            ):
                continue

            new_node = Node(
                current, new_position, current.g,
                abs(new_position[0] - end_loc[0]) +
                abs(new_position[1] - end_loc[1])
            )

            # Check if position is already present in open list
            if any(node.position == new_node.position for _, node in open_list):
                continue

            heapq.heappush(open_list, (new_node.f, new_node))

    return []


# matrix = [
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 1],
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0]
# ]
# start_loc = (0, 0)
# end_loc = (5, 5)

matrix = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]

start_pos = (0, 0)
end_pos = (3, 3)

path = a_star(matrix, start_pos, end_pos)

if path:
    print("Path found:", path)
else:
    print("No path found.")
