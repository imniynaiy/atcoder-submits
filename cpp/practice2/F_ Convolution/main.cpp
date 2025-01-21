#include <bits/stdc++.h>
#include <atcoder/convolution>
using namespace std;
using namespace atcoder;

int main() {
    int N, M;
    cin >> N >> M;
    vector<long long> A(N), B(M);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < M; ++i) cin >> B[i];
    
    vector<long long> C = convolution(A, B);
    for (int i = 0; i < N + M - 1; ++i) cout << C[i] << " ";
    cout << endl;
}