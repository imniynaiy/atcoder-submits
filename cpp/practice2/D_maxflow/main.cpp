#include <bits/stdc++.h>
#include <atcoder/maxflow>
using namespace std;
using namespace atcoder;

// 上下左右を表すベクトル
const vector<int> DX = {1, 0, -1, 0};
const vector<int> DY = {0, 1, 0, -1};

int main()
{
    // 入力受け取り
    int N, M;
    cin >> N >> M;
    vector<string> grid(N);
    for (int i = 0; i < N; ++i)
        cin >> grid[i];

    auto index = [&](int i, int j) -> int
    { return i * M + j; };

    // フローネットワークを作る
    // 各マスの番号を 0, 1, ..., NM-1 とし、超頂点の番号を S = NM, T = NM+1 とする
    mf_graph<int> G(N * M + 2);
    int S = N * M, T = N * M + 1;

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            // 黒色マスならば、上下左右の 4 マスと辺を結んでいく
            if ((i + j) % 2 == 0)
            {
                for (int dir = 0; dir < 4; ++dir)
                {
                    int i2 = i + DX[dir], j2 = j + DY[dir];
                    if (i2 < 0 || i2 >= N || j2 < 0 || j2 >= M)
                        continue;

                    // どちらも空マスならば、ドミノを置けるので、辺を結ぶ
                    if (grid[i][j] == '.' && grid[i2][j2] == '.')
                    {
                        G.add_edge(index(i, j), index(i2, j2), 1);
                    }
                }
            }

            // 超頂点 S から黒色マスへの辺を結ぶ
            if ((i + j) % 2 == 0 && grid[i][j] == '.')
            {
                G.add_edge(S, index(i, j), 1);
            }

            // 白色マスから超頂点 T への辺を結ぶ
            if ((i + j) % 2 == 1 && grid[i][j] == '.')
            {
                G.add_edge(index(i, j), T, 1);
            }
        }
    }

    // 最大流を流す
    int max_flow = G.flow(S, T);

    // フロー値が 1 となった辺を特定して、ドミノタイリングを復元する
    const auto &edges = G.edges();
    for (const auto &e : edges)
    {
        // 辺 e が超頂点に接続するものや、フロー値が 0 であるものはスキップ
        if (e.from == S || e.to == T || e.flow == 0)
            continue;

        // 辺 e の両端点に対応するマス
        int ifrom = e.from / M, jfrom = e.from % M;
        int ito = e.to / M, jto = e.to % M;

        // ドミノを置く
        if (ifrom == ito)
        {
            // ドミノを横に配置する場合
            if (jfrom > jto)
                swap(jfrom, jto);
            grid[ifrom][jfrom] = '>';
            grid[ito][jto] = '<';
        }
        else
        {
            // ドミノを縦に配置する場合
            if (ifrom > ito)
                swap(ifrom, ito);
            grid[ifrom][jfrom] = 'v';
            grid[ito][jto] = '^';
        }
    }

    // 出力
    cout << max_flow << endl;
    for (int i = 0; i < N; ++i)
        cout << grid[i] << endl;
}