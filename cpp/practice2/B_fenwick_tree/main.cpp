#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;

    atcoder::fenwick_tree<long long> fw(N);

    int input;
    for (int i = 0; i < N; ++i) {
        cin >> input;
        fw.add(i, input);
    }

    int a, b, c;
    for (int i = 0; i < Q; ++i) {
        cin >> a >> b >> c;
        if (a == 0)
            fw.add(b, c);
        else
            cout << fw.sum(b,c) << endl;
    }
}