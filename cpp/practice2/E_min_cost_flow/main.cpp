#include <bits/stdc++.h>
#include <atcoder/mincostflow>
using namespace std;
using namespace atcoder;

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> A(N * N);
    for (int i = 0; i < N * N; i++)
    {
        cin >> A[i];
    }

    long long bignum = 1000000000;

    mcf_graph<int, long long> G(N * 2 + 2);
    for (int i = 0; i < N; i++)
    {
        G.add_edge(N * 2, i, K, 0);
        // cout << N * 2 << ' ' << i << ' ' << K << ' ' << 0 << ' ' << endl;
        for (int j = 0; j < N; j++)
        {
            G.add_edge(i, N + j, 1, bignum - A[i * N + j]);
            // cout << i << ' ' << N + j << ' ' << 1 << ' ' << -A[i * K + j] << ' ' << endl;
        }
    }
    for (int j = 0; j < N; j++)
    {
        G.add_edge(N + j, N * 2 + 1, K, 0);
        // cout << N + j << ' ' << N * 2 + 1 << ' ' << K << ' ' << 0 << ' ' << endl;
    }
    G.add_edge(N + N, N * 2 + 1, N*K, bignum);
    auto min_flow = G.flow(N * 2, N * 2 + 1, N*K);
    // cout << min_flow.second << endl;
    // auto slope = G.slope(N * 2, N * 2 + 1, K);
    auto edges = G.edges();
    for (const auto &e : edges)
    {
        if (e.from == N * 2 || e.to == N * 2 + 1)
        {
            continue;
        }
        A[N * e.from + e.to % N] = e.flow;
    }
    cout << (min_flow.first * bignum - min_flow.second) << endl;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (A[i * N + j] == 1)
            {
                cout << 'X';
            }
            else
            {
                cout << '.';
            }
        }
        cout << endl;
    }
}