#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max(); // Бесконечность

// Структура для представления ребра графа
struct Edge {
    int to;     // Вершина, в которую ведет ребро
    int weight; // Вес ребра
};

// Функция для выполнения алгоритма Дейкстры
vector<int> dijkstra(int start, const vector<vector<Edge>>& graph) {
    int n = graph.size();
    vector<int> distance(n, INF); // Вектор расстояний
    distance[start] = 0;           // Расстояние до стартовой вершины равно 0

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // Мини-куча
    pq.push({0, start}); // Добавляем стартовую вершину в очередь

    while (!pq.empty()) {
        int current_distance = pq.top().first; // Текущее расстояние
        int current_vertex = pq.top().second;   // Текущая вершина
        pq.pop();

        // Если текущее расстояние больше, чем уже найденное, пропускаем
        if (current_distance > distance[current_vertex]) {
            continue;
        }

        // Проходим по всем соседям текущей вершины
        for (const Edge& edge : graph[current_vertex]) {
            int new_distance = current_distance + edge.weight;
            // Если найдено более короткое расстояние до соседа
            if (new_distance < distance[edge.to]) {
                distance[edge.to] = new_distance;
                pq.push({new_distance, edge.to}); // Добавляем соседа в очередь
            }
        }
    }

    return distance; // Возвращаем вектор расстояний
}

int main() {
    // Пример графа: 0 - стартовая вершина
    vector<vector<Edge>> graph = {
        {{1, 4}, {2, 1}}, // Вершина 0
        {{3, 1}},         // Вершина 1
        {{1, 2}, {3, 5}}, // Вершина 2
        {}                // Вершина 3
    };

    int start_vertex = 0;
    vector<int> distances = dijkstra(start_vertex, graph);

    cout << "Расстояния от вершины " << start_vertex << " до остальных вершин:" << endl;
    for (int i = 0; i < distances.size(); ++i) {
        if (distances[i] == INF) {
            cout << "До вершины " << i << " невозможно добраться." << endl;
        } else {
            cout << "Расстояние до вершины " << i << ": " << distances[i] << endl;
        }
    }

    return 0;
}
