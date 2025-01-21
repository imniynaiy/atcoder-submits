#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;
using namespace atcoder;

struct Node {
    long zeros, ones;
    long val;
    Node(long z = 0, long o = 0, long v = 0) : zeros(z), ones(o), val(v) {}
};

Node op(Node x, Node y) { return Node(x.zeros + y.zeros, x.ones + y.ones, x.val + y.val + x.ones * y.zeros); }

Node e() { return Node(0, 0, 0); }

using Act = bool;

Node mapping(Act f, Node x) {
    //颠倒后的「颠倒数」应该是将所有可能的 0 和 1 的对数（x.ones * x.zeros）减去原来的「颠倒数」，因为原来不满足条件的对数在颠倒后满足了条件，反之亦然。
    if (f) return Node(x.ones, x.zeros, x.ones * x.zeros - x.val);
    else return x;
}

Act composition(Act g, Act f) {
    if (g) f = !f;
    return f;
}

Act id() { return false; }

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<Node> a(N);
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;
        if (x) a[i] = Node{0, 1, 0};
        else a[i] = Node{1, 0, 0};
    }
    lazy_segtree<Node, op, e, Act, mapping, composition, id> seg(a);
    for (int i = 0; i < Q; ++i) {
        int t, l, r;
        cin >> t >> l >> r;
        --l;
        if (t == 1) {
            seg.apply(l, r, true);
        } else {
            Node res = seg.prod(l, r);
            cout << res.val << endl;
        }
    }
    
}