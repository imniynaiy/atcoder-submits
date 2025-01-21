#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
#include <atcoder/modint>
using namespace std;
using namespace atcoder;

using mint = modint998244353;

struct Node {
    mint val;
    int siz;
    Node(mint v = 0, int s = 0) : val(v), siz(s) {}
};

Node op(Node x, Node y) { return Node(x.val + y.val, x.siz + y.siz); }

Node e() { return Node(0, 0); }

struct Act {
    mint b, c;
    Act(mint b = 0, mint c = 0) : b(b), c(c) {}
};

Node mapping(Act f, Node x) {
    return Node(f.b * x.val + f.c * x.siz, x.siz);
}

Act composition(Act f, Act g) {
    return Act(f.b * g.b, f.b * g.c + f.c);
}

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
    lazy_segtree<Node, op, e, Act, mapping, composition, id> seg(a);
    for (int i = 0; i < Q; ++i) {
        int t;
        cin >> t;
        if (t == 0) {
            int l, r, b, c;
            cin >> l >> r >> b >> c;
            seg.apply(l, r, Act(b,c));
        } else {
            int l, r;
            cin >> l >> r;
            Node res = seg.prod(l, r);
            cout << res.val.val() << endl;
        }
    }
    
}