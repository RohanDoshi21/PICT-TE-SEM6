#include <iostream>
#include <queue>

using namespace std;

class Graph
{
    /// Hold the runtime dimension of adjecency matrix @c limit=20
    int dimensions;

    /// This is a adjecency matrix hold maximum of 20*20 elements
    int matrix[20][20];

    int visited[20];

public:
    Graph()
    {
        cout << "Enter Matrix dimensions ";
        cin >> dimensions;

        for (int i = 0; i < dimensions; i++)
        {
            for (int j = 0; j < dimensions; j++)
            {
                cin >> matrix[i][j];
            }
        }
    }

    void DFS(int node = 0)
    {
        cout << node << " ";
        visited[node] = true;

        for (int i = 0; i < dimensions; i++)
        {
            if (matrix[node][i] > 0 && !visited[i])
                DFS(i);
        }
    }

    /**
       *  @brief  This function should be called before calling @c DFS() or @c BFS()
    */
    void clearVisited()
    {
        for (int i = 0; i < dimensions; i++)
        {
            visited[i] = false;
        }
    }

    void BFS(int source = 0)
    {
        queue<int> q;
        q.push(source);

        visited[source] = true;

        while (!q.empty())
        {
            int element = q.front();
            q.pop();

            cout << element << " ";

            for (int i = 0; i < dimensions; i++)
            {
                if ((!visited[i]) and matrix[element][i] > 0)
                {
                    q.push(i);
                    visited[i] = true;
                }
            }
        }
    }
};

int main()
{
    Graph g1;

    g1.clearVisited();
    cout << "DFS: ";
    g1.DFS();
    cout << endl;

    g1.clearVisited()
    cout << "BFS: ";
    g1.BFS();
    cout << endl;

    return 0;
}

/*
Sample Test cases:

5
0 0 1 2 3
0 0 1 1 0
1 1 0 0 1
2 1 0 0 0
3 0 1 0 0

Source = 1
DFS: 1 2 0 3 4
BFS: 1 2 3 0 4

Source = 0
*/
