#include <bits/stdc++.h>
#include <atcoder/string>
using namespace std;

int main() {
    string S;
    cin >> S;
    long long N = S.size();

    // Suffix Array の構築
    vector<int> sa = atcoder::suffix_array(S);
    //lcp = longest common prefix
    vector<int> lcp = atcoder::lcp_array(S, sa);

    // 高さ配列の総和を求める
    long long sum = 0;
    for (auto v : lcp) sum += v;

    // 答え
    cout << N*(N+1)/2 - sum << endl;
}