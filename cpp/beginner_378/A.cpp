#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b,c,d;
    int ca = 0, cb =0, cc = 0;
    cin >> a >> b;
    if (b == a) {
        ca++;
    }
    cin >> c;
    if (c == a) {
        ca++;
    } else if (c == b){
        cb++;
    }
    cin >> d;
    if (d == a) {
        ca++;
    } else if (d == b){
        cb++;
    } else if (c == d){
        cc++;
    }
    if (ca == 3) {
        cout << 2 <<endl;
    }
    if (ca == 2 || cb == 2) {
        cout << 1 << endl;
    }
    if (ca == 1) {
        if (cb == 1 || cc == 1) {
            cout << 2 << endl;
        } else {
            cout << 1 << endl;
        }
    }
    if (ca == 0 && cb == 0 && cc == 1){
        cout << 1 <<endl;
    }
    if (ca == 0 && cb == 0 && cc == 0){
        cout << 0 << endl;
    }
    if (ca == 0 && cb == 1 && cc == 0){
        cout << 1 << endl;
    }
}
    
    