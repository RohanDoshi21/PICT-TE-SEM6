# Refer https://www.youtube.com/watch?v=wuVwUK25Rfc

# 1. Backtracking only
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def is_safe(self, current_vertex, result_color, color):
        for i in range(self.vertices):
            if self.graph[current_vertex][i] == 1 and result_color[i] == color:
                return False
        return True

    def graph_coloring_util(self, no_of_colors, result_color, current_vertex):
        # Exit Condition
        if current_vertex == self.vertices:
            return True

        for color in range(1, no_of_colors + 1):
            if self.is_safe(current_vertex, result_color, color):
                result_color[current_vertex] = color
                if self.graph_coloring_util(no_of_colors, result_color, current_vertex + 1):
                    return True
                # Remove the color if not true (backtrack)
                result_color[current_vertex] = 0

        return False

    def graph_coloring(self, no_of_colors):
        # This is the result
        result_color = [0] * self.vertices
        if not self.graph_coloring_util(no_of_colors, result_color, 0):
            print("No solution exists.")
            return False

        print("Graph coloring possible with", no_of_colors, "colors.")
        print("Vertex   Color")
        for i in range(self.vertices):
            print(i, "\t", result_color[i])

        return True


# Test case 1
g1 = Graph(4)
g1.graph = [[0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]]
g1.graph_coloring(3)
print()

# Test case 2
g2 = Graph(5)
g2.graph = [[0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [1, 1, 1, 0, 1],
            [0, 1, 0, 1, 0]]
g2.graph_coloring(2)


# Theory
"""
    1. Backtracking
        -> DFS strategy, all possible solutions are explored
        -> It systematically builds a solution and backtracks when a conflict is encountered, trying alternative choices

    2. Branch and Bound
        -> DFS but with bounds
        -> t explores the search space selectively, discarding branches that are known to lead to solutions worse than the current best solution
        -> Branch and Bound, with its pruning mechanism, reduces the search space significantly by eliminating unpromising branches.
        -> More Efficient
"""