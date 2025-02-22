#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<unordered_set<int>> adjList(n);
    int count = 0;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        if (a > b) {
            swap(a, b);
        }
        if (a == b) {
            count += 1;
        } else if (adjList[a-1].count(b-1)) {
            count += 1;
        } else {
            adjList[a-1].insert(b-1);
        }
    }

    cout << count << endl;

    return 0;
}