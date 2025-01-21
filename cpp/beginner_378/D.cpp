#include <bits/stdc++.h>
using namespace std;

// 上下左右を表すベクトル
const vector<int> DX = {1, 0, -1, 0};
const vector<int> DY = {0, 1, 0, -1};

vector<bool>* visitedPtr = nullptr;

vector<string>* gridPtr = nullptr;

int H,W,K, ans = 0;

void rec(int i, int j, int k) {
    if (k == K) {
        ans += 1;
        return;
    }
    (*visitedPtr)[i * W + j] = true;
    int ni, nj;
    for (int dir = 0; dir < 4; dir++)
    {
        ni = i + DX[dir];
        nj = j + DY[dir];
        if (ni >= 0 && ni < H && nj >= 0 && nj < W && (*gridPtr)[ni][nj] == '.' && !(*visitedPtr)[ni * W + nj]) {
            rec(ni, nj, k+1);
        }
    }
    (*visitedPtr)[i * W + j] = false;
}

int main()
{
    cin >> H >> W >> K;
    gridPtr = new vector<string>(H);
    for (int i = 0; i < H; ++i)
        cin >> (*gridPtr)[i];

    visitedPtr = new vector<bool>(H * W);

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            if ((*gridPtr)[i][j] == '.') {
                rec(i, j, 0);
            }
        }
        
    }

    cout << ans << endl;    
}