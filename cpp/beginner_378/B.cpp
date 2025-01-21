#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long> r(N);
    vector<long> q(N);
    for (int i = 0; i < N; i++)
    {
        cin >> q[i] >> r[i]; 
    }
    int Q, t, d, qc,rc;
    cin >> Q;
    for (int i = 0; i < Q; i++)
    {
        cin >> t >> d;
        t--;
        qc = q[t];
        rc = r[t];
        if (d % qc) {
            if (d % qc > rc) {
                cout << (d / qc + 1) * qc + rc << endl;
            } else {
                cout << (d / qc) * qc + rc << endl;
            }
        } else {
            cout << d + rc << endl;
        }
    }
}
    
    