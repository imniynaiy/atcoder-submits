#include <bits/stdc++.h>
#include <atcoder/scc>
using namespace std;
using namespace atcoder;

int main() {
    int N, M;
    cin >> N >> M;
    
    // SCC を適用するためのグラフを構築する
    scc_graph G(N);
    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        G.add_edge(u, v);
    }
    
    // SCC
    auto scc = G.scc();
    
    // 出力
    cout << scc.size() << endl;
    for (auto list : scc) {
        cout << list.size();
        for (auto v : list) cout << " " << v;
        cout << endl;
    }
}