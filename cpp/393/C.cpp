#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<bool>> mat(n, vector<bool>(n, false));
    int count = 0;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        if (a > b) {
            swap(a, b);
        }
        if (a == b) {
            count += 1;
        } else if (mat[a-1][b-1]) {
            count += 1;
        } else {
            mat[a-1][b-1] = true;
        }
    }

    cout << count << endl;

    return 0;
}