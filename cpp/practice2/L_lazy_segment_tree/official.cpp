#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;
using namespace atcoder;

/* セグメント木のための構造体と、二項演算関数 op と、単位元関数 e */
struct Node {
    long long zero, one, tentou;  // 区間内部の 0 の個数、1 の個数、転倒数
};

// 二項演算
Node op(Node x, Node y) {
    return Node{x.zero + y.zero,
                x.one + y.one,
                x.tentou + y.tentou + x.one * y.zero};
}

// 単位元
Node e() { return Node{0, 0, 0}; }

/* 遅延評価のための型と、作用関数 mapping と、作用の合成関数 composition と、単位元関数 id() */
using Act = bool;  // 区間反転するかどうか

// 作用関数
Node mapping(Act f, Node x) {
    if (f) return Node{x.one, x.zero, x.one * x.zero - x.tentou};
    else return x;
}

// 作用の合成関数
Act composition(Act g, Act f) {
    if (g) f = !f;
    return f;
}

// 作用の単位元
Act id() { return false; }

int main() {
    // 入力
    int N, Q;
    cin >> N >> Q;
    vector<Node> A(N);
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;
        if (x) A[i] = Node{0, 1, 0};
        else A[i] = Node{1, 0, 0};
    }
    
    // 遅延評価セグメント木のセットアップ
    lazy_segtree<Node, op, e, Act, mapping, composition, id> seg(A);
    
    // クエリ処理
    while (Q--) {
        int t, l, r;
        cin >> t >> l >> r;
        --l;
        if (t == 1) {
            seg.apply(l, r, true);
        } else {
            Node res = seg.prod(l, r);
            cout << res.tentou << endl;
        }
    }
}