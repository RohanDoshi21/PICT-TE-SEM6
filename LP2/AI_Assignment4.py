# Refer https://www.youtube.com/watch?v=wuVwUK25Rfc

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def is_safe(self, current_vertex, result_color, c):
        for i in range(self.V):
            if self.graph[current_vertex][i] == 1 and result_color[i] == c:
                return False
        return True

    def graph_coloring_util(self, no_of_colors, result_color, current_vertex):
        # Exit Condition
        if current_vertex == self.V:
            return True

        for c in range(1, no_of_colors + 1):
            if self.is_safe(current_vertex, result_color, c):
                result_color[current_vertex] = c
                if self.graph_coloring_util(no_of_colors, result_color, current_vertex + 1):
                    return True
                result_color[current_vertex] = 0

    def graph_coloring(self, no_of_colors):
        # This is the result
        result_color = [0] * self.V
        if not self.graph_coloring_util(no_of_colors, result_color, 0):
            print("No solution exists.")
            return False

        print("Graph coloring possible with", no_of_colors, "colors.")
        print("Vertex   Color")
        for i in range(self.V):
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
