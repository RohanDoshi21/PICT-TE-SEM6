// Refer: https://www.youtube.com/watch?v=YfnDKFm6GHM

#include <iostream>
using namespace std;
#define INT_MAX 2147483647

class Graph
{
    int adjMatrix[20][20];
    int Nodes;
    int Edges;
    int weight;

public:
    void add_edge(int source, int destination, int weight)
    {
        adjMatrix[source][destination] = weight;
    }

    Graph(int Nodes, int Edges)
    {
        this->Nodes = Nodes;
        this->Edges = Edges;
        for (int i = 0; i < Nodes; i++)
        {
            for (int j = 0; j < Nodes; j++)
            {
                adjMatrix[i][j] = 0;
            }
        }
        weight = 0;
    }
    void Display()
    {
        for (int i = 0; i < Nodes; i++)
        {
            for (int j = 0; j < Nodes; j++)
            {
                if (adjMatrix[i][j] != 0)
                {
                    cout << i << " - " << j << " :  " << adjMatrix[i][j] << endl;
                }
            }
        }
    }
    void Create()
    {
        int source;
        int destination;
        int weight;
        for (int i = 0; i < Edges; i++)
        {
            cout << "Enter Source: ";
            cin >> source;
            cout << "Enter Destination: ";
            cin >> destination;
            cout << "Enter Weight: ";
            cin >> weight;
            add_edge(source, destination, weight);
            add_edge(destination, source, weight);
        }
    }
    int heuristic(int source, int destination)
    {
        return abs(source - destination);
    }

    void Prims()
    {
        int edges_no = 0;
        int selected[Nodes];

        // initialize all the postions to false initially
        for (int i = 0; i < Nodes; i++)
        {
            selected[i] = false;
        }
        // Start from the first element
        // so mark the first element to be visited
        selected[0] = true;
        int min = INT_MAX;
        int x = 0;
        int y = 0;

        // from each edge traverse to all other edges
        // E = < V - 1
        while (edges_no < Nodes - 1)
        {
            // Let the min value be the maximum element that is present
            min = INT_MAX; // holds the min weight
            x = 0;         // row of the MST element that we need to display
            y = 0;         // Column of MST element that we need to display

            // traverse the row
            for (int i = 0; i < Nodes; i++)
            {
                // traverse the column elements only for the vertex that we are visiting
                if (selected[i])
                {
                    // traverse the column
                    for (int j = 0; j < Nodes; j++)
                    {
                        // Select only Non-Zero and Non-Visited element to display
                        if (!selected[j] && adjMatrix[i][j])
                        {
                            // Find out the min element from the column
                            int total = adjMatrix[i][j] + heuristic(i, j);
                            if (min > total)
                            {
                                min = total;
                                // Store the position of Min Element in X and Y
                                x = i;
                                y = j;
                            }
                        }
                    }
                }
            }

            // The Minimum element will be G[X][Y]
            cout << x << " - " << y << " :  " << adjMatrix[x][y];
            weight += adjMatrix[x][y];
            cout << endl;

            // Make the selected column element to be visited
            selected[y] = true;

            // Increment the edge_no
            edges_no++;
        }
        cout << "Weight of minimum spanning tree: " << weight << endl;
    }
};

int main()
{
    int edges = 7;
    int vertices = 5;
    Graph graph(vertices, edges);

    // Add edges and their weights
    graph.add_edge(0, 1, 2);
    graph.add_edge(0, 3, 6);
    graph.add_edge(1, 2, 3);
    graph.add_edge(1, 3, 8);
    graph.add_edge(1, 4, 5);
    graph.add_edge(2, 4, 7);
    graph.add_edge(3, 4, 9);

    cout << "Graph Edges:" << endl;
    graph.Display();
    cout << endl;

    cout << "Minimum Spanning Tree Edges (Prim's algorithm):" << endl;
    graph.Prims();
}

/*
    Greedy Search Algorithm
    -> Local Search Algorithm
    -> Not optimal
    -> Select the next node which is adjacent to the current node and has the least cost/distance from the current node.
    -> Not Complete
*/
