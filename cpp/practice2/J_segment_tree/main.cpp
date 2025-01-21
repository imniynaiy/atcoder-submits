#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int e()
{
    return -1;
}

int op(int a, int b) {
    return max(a,b);
}

int target;

bool f(int v) { return v < target; }

int main()
{
    int N, Q;
    cin >> N >> Q;
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    segtree<int, op, e> seg(A);
    for (int i = 0; i < Q; i++)
    {
        int T, X, V;
        cin >> T >> X >> V;
        if (T == 1)
        {
            seg.set(X - 1, V);
        }
        else if (T == 2)
        {
            cout << seg.prod(X-1, V) << endl;
        }
        else if (T == 3)
        {
            target = V;
            cout << seg.max_right<f>(X-1) + 1 << endl;
        }
    }
}