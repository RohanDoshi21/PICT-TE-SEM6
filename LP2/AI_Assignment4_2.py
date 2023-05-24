# 2. Branch and Bound
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def is_safe(self, current_vertex, result_color, color):
        for i in range(self.vertices):
            if self.graph[current_vertex][i] == 1 and result_color[i] == color:
                return False
        return True

    def get_bound(self, current_vertex, result_color, no_of_colors):
        used_colors = set()
        for i in range(self.vertices):
            if self.graph[current_vertex][i] == 1 and result_color[i] != 0:
                used_colors.add(result_color[i])
        return no_of_colors - len(used_colors)

    def graph_coloring_util(self, no_of_colors, result_color, current_vertex):
        if current_vertex == self.vertices:
            return True

        for color in range(1, no_of_colors + 1):
            if self.is_safe(current_vertex, result_color, color):
                result_color[current_vertex] = color

                bound = self.get_bound(
                    current_vertex, result_color, no_of_colors)
                if bound >= 0:  # Updated bound check condition
                    if self.graph_coloring_util(no_of_colors, result_color, current_vertex + 1):
                        return True

                result_color[current_vertex] = 0

        return False

    def graph_coloring(self, no_of_colors):
        result_color = [0] * self.vertices

        if self.graph_coloring_util(no_of_colors, result_color, 0):
            print("Graph coloring possible with", no_of_colors, "colors.")
            print("Vertex   Color")
            for i in range(self.vertices):
                print(i, "\t", result_color[i])
        else:
            print("No solution exists.")

        return True


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
