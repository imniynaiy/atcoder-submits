#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<long> X(M), A(M);
    for (long i = 0; i < M; ++i) {
        cin >> X[i];
    }
    for (long i = 0; i < M; ++i) {
        cin >> A[i];
    }

    long long count = 0;
    if (X[0] != 1) {
        cout << -1 << endl;
        return 0;
    }

    for (long i = 0; i < M - 1; ++i) {
        long to_move = X[i + 1] - X[i];
        long extra = A[i] - to_move;
        long long steps = to_move * (to_move - 1) / 2 + to_move * extra;
        count += steps;

        if (extra < 0) {
            cout << -1 << endl;
            return 0;
        }
        X[i + 1] += extra;
    }

    long to_move = N - X[M - 1];
    long extra = A[M - 1] - to_move;
    long long steps = to_move * (to_move - 1) / 2 + to_move * extra;
    count += steps;

    if (extra < 0) {
        cout << -1 << endl;
        return 0;
    }

    cout << count << endl;
    return 0;
}