#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;

int main()
{
    int t;
    cin >> t;

    int n, m, a, b;
    for (int i = 0; i < t; ++i)
    {
        cin >> n >> m >> a >> b;
        cout << atcoder::floor_sum(n, m, a, b) << endl;
    }
}