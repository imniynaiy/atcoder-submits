#include <bits/stdc++.h>
#include <atcoder/mincostflow>
using namespace std;
using namespace atcoder;

void ACL_practice_E() {
    // 十分大きな値
    const long long B = 1LL<<40;
    
    // 入力
    int N, K;
    cin >> N >> K;
    vector<vector<long long>> A(N, vector<long long>(N));
    for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) cin >> A[i][j];
    
    // フローネットワークを作る
    // 行番号に対応する頂点を 0, 1, ..., N-1、列番号に対応する頂点を N, N+1, ..., 2N-1 とする
    // 超頂点の番号を S = 2N, T = 2N+1 とする
    mcf_graph<int, long long> G(N * 2 + 2);
    int S = N * 2, T = N * 2 + 1;
    
    // 行と列を結ぶ
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            // 容量 1、コスト B - A[i][j]
            G.add_edge(i, j + N, 1, B - A[i][j]);
        }
    }
    
    // 超頂点
    for (int i = 0; i < N; ++i) {
        G.add_edge(S, i, K, 0);  // 容量 K, コスト 0
        G.add_edge(i + N, T, K, 0);  // 容量 K, コスト 0
    }
    
    // バイパス
    G.add_edge(S, T, N * K, B);
    
    // 流量 N * K の最小費用流を流す (最大流量も受け取るが N * K になることは分かっている)
    auto [max_flow, min_cost] = G.flow(S, T, N * K);
    
    // 復元する
    vector<string> grid(N, string(N, '.'));
    const auto &edges = G.edges();
    for (const auto &e : edges) {
        // 超頂点が絡む辺や、フローの流れなかった辺はスキップ
        if (e.from == S || e.to == T || e.flow == 0) continue;
        
        // 行 e.from、列 e.to - N が選ばれる
        grid[e.from][e.to - N] = 'X';
    }
    
    // 出力
    cout << B * N * K - min_cost << endl;
    for (int i = 0; i < N; ++i) cout << grid[i] << endl;
}

int main() {
    ACL_practice_E();
}