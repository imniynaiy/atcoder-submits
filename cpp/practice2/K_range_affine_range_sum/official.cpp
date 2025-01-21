#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
#include <atcoder/modint>
using namespace std;
using namespace atcoder;

/* セグメント木のための構造体と、二項演算関数 op と、単位元関数 e */
using mint = modint998244353;
struct Node {
    mint val;
    int siz;
    Node(mint v = 0, int s = 0) : val(v), siz(s) {}
};

// 二項演算
Node op(Node x, Node y) { return Node(x.val + y.val, x.siz + y.siz); }

// 単位元
Node e() { return Node(0, 0); }

/* 遅延評価のための構造体と、作用関数 mapping と、作用の合成関数 composition と、単位元関数 id() */
struct Act {
    mint b, c;
    Act(mint b = 0, mint c = 0) : b(b), c(c) {}
};

// 作用関数
Node mapping(Act f, Node x) {
    return Node(f.b * x.val + f.c * x.siz, x.siz);
}

// 作用の合成関数：g.b((f.b)x + f.c) + g.c = (g.b f.b)x + g.b f.c + g.c
Act composition(Act g, Act f) {
    return Act(g.b * f.b, g.b * f.c + g.c);
}

// 作用の単位元
Act id() { return Act(1, 0); }

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<Node> a(N);
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;
        a[i] = Node(x, 1);
    }
    
    // 遅延評価セグメント木のセットアップ
    lazy_segtree<Node, op, e, Act, mapping, composition, id> seg(a);
    
    // クエリ処理
    while (Q--) {
        int t;
        cin >> t;
        if (t == 0) {
            int l, r, c, d;
            cin >> l >> r >> c >> d;
            seg.apply(l, r, Act(c, d));
        } else {
            int l, r;
            cin >> l >> r;
            Node res = seg.prod(l, r);
            cout << res.val.val() << endl;
        }
    }
}