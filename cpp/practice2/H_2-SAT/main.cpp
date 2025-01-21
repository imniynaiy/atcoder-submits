#include <bits/stdc++.h>
#include <atcoder/scc>
using namespace std;
using namespace atcoder;

struct TwoSATSolver : scc_graph {
    // input
    int num_variables;
    
    // result
    vector<int> solution;

    vector<int> cmp;
    
    // constructor
    TwoSATSolver(int N = 0) : scc_graph(N * 2), num_variables(N), solution(N), cmp(N*2) {}
    
    // リテラルの否定をとる
    inline int take_not(int x) {
        if (x < num_variables) return x + num_variables;
        else return x - num_variables;
    }
    
    // closure の追加
    void add_constraint(bool is_x_true, int x, bool is_y_true, int y) {
        assert(x >= 0 && x < num_variables);
        assert(y >= 0 && y < num_variables);
        if (!is_x_true) x = take_not(x);
        if (!is_y_true) y = take_not(y);
        add_edge(take_not(x), y);
        add_edge(take_not(y), x);
    }
    
    // main solver
    auto solve() {
        auto s = scc();
        int count = 0;
        for (auto list: s){
            for (auto v: list) {
                cmp[v] = count;
            }
            count++;
        }
        for (int i = 0; i < num_variables; ++i) {
            // no solution
            if (cmp[i] == cmp[take_not(i)]) {
                return vector<int>();
            }
            solution[i] = (cmp[i] > cmp[take_not(i)]);
        }
        return solution;
    }
};

int main() {
    int N, D;
    cin >> N >> D;
    
    vector<int> X(N);
    vector<int> Y(N);
    vector<int> Result(N);

    TwoSATSolver solver(N);

    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i];
        for (int j = 0; j < i; j++) {
            if (abs(X[i] - X[j]) < D) {
                solver.add_constraint(false, i, false, j);
            }
            if (abs(X[i] - Y[j]) < D) {
                solver.add_constraint(false, i, true, j);
            }
            if (abs(Y[i] - X[j]) < D) {
                solver.add_constraint(true, i, false, j);
            }
            if (abs(Y[i] - Y[j]) < D) {
                solver.add_constraint(true, i, true, j);
            }
        }
    }

    auto res = solver.solve();

    if (res.empty()) cout << "No" << endl;
    else {
        cout << "Yes" << endl;
        for (int i = 0; i < N; ++i) {
            cout << (res[i] ? X[i] : Y[i]) << endl;
        }
    }
}