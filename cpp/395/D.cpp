#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> BN(n);
    unordered_map<int, vector<int>> NB;

    for (int i = 0; i < n; ++i) {
        BN[i] = i + 1;
        NB[i + 1] = {i + 1};
    }

    for (int i = 0; i < q; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            int a, b;
            cin >> a >> b;
            BN[a - 1] = b;
            NB[b].push_back(a);
        } else if (type == 2) {
            int a, b;
            cin >> a >> b;
            for (int j : NB[a]) {
                BN[j - 1] = b;
            }
            for (int j : NB[b]) {
                BN[j - 1] = a;
            }
            swap(NB[a], NB[b]);
        } else if (type == 3) {
            int a;
            cin >> a;
            cout << BN[a - 1] << endl;
        }
    }

    return 0;
}