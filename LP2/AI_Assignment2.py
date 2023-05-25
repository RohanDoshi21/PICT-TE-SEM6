import heapq


class Node:
    def __init__(self, parent, position, g, h):
        self.parent = parent
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def a_star(matrix, start_loc, end_loc):
    open_list = []
    closed_list = []

    start_node = Node(None, start_loc, 0, 0)
    end_node = Node(Node, end_loc, 0, 0)

    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:

        # Pop the node with the lowest priority from the open list
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        if current_node.position == end_node.position:  # Check if we have reached the goal
            path = []
            current = current_node
            while current:  # Reconstruct the path by traversing the parent pointers
                path.append(current.position)
                current = current.parent
            path.reverse()
            return path  # Return the path

        # Possible neighbor directions (left, right, up, down)
        delta_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for delta in delta_directions:
            node_position = (
                current_node.position[0] + delta[0], current_node.position[1] + delta[1])  # Calculate the neighbor position

            # Check if the neighbor is out of bounds or blocked by an obstacle
            if (
                node_position[0] < 0 or node_position[0] >= len(matrix) or
                node_position[1] < 0 or node_position[1] >= len(matrix[0]) or
                matrix[node_position[0]][node_position[1]] != 0
            ):
                continue

            new_node = Node(
                current_node, node_position, current_node.g + 1,
                abs(node_position[0] - end_loc[0]) +
                abs(node_position[1] - end_loc[1])
            )  # Create a new node for the neighbor

            # Check if the new node is already in the closed list
            if new_node in closed_list:
                continue

            # Check if the new node is already in the open list
            if any(node.position == new_node.position for _, node in open_list):
                continue

            heapq.heappush(open_list, (new_node.f, new_node))

    return []


matrix = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
start_loc = (0, 0)
end_loc = (5, 5)
path = a_star(matrix, start_loc, end_loc)

if path:
    print("Path found:", path)
else:
    print("No path found.")
