#include <iostream>
#include <list>

using namespace std;

int main() {
    int n;
    cin >> n;
    list<int> myList = {};
    int p;
    for (int i = 0; i < n; ++i) {
        cin >> p;
        auto it = myList.begin();
        advance(it, p-1);
        myList.insert(it, i+1);
    }

    for (int val : myList) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}