#include <bits/stdc++.h>
#include <atcoder/convolution>
#include <atcoder/modint>
using namespace std;
using namespace atcoder;

using mint = modint998244353;

int main() {
    int N, M;
    cin >> N >> M;
    vector<mint> A(N), B(M);
    for (int i = 0; i < N; ++i) {
        long long a;
        cin >> a;
        A[i] = a;
    }
    for (int i = 0; i < M; ++i) {
        long long b;
        cin >> b;
        B[i] = b;
    }
    
    vector<mint> C = convolution(A, B);
    for (int i = 0; i < N + M - 1; ++i) cout << C[i].val() << " ";
    cout << endl;
}