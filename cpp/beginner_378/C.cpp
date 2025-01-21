#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<long> A(N);
    vector<long> B(N);
    map<long, int> map;
    long input;
    for (int i = 0; i < N; i++)
    {
        cin >> input;
        auto it = map.find(input);
        if (it == map.end())
        {
            cout << -1 << ' ';
            map[input] = i;
        }
        else
        {
            cout << it->second + 1 << ' ';
            it -> second = i;
        }
        
    }
    cout << endl;
}
