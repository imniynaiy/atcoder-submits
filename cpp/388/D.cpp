#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);

    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    for (int i = 0; i < N; ++i) {
        int to_dis;
        if (A[i] < N - 1 - i) {
            to_dis = A[i];
        } else {
            to_dis = N - 1 - i;
        }
        A[i] -= to_dis;
        for (int j = i+1; j < i+to_dis+1; ++j) {
            A[j] += 1; 
        }
    }

    for (int i = 0; i < N; ++i) {
        cout << A[i];
        if (i < N - 1) cout << " ";
    }
    cout << endl;

    return 0;
}