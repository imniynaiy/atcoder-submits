#include <iostream>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> A(n);
    vector<int> K(n);

    unordered_map<int, vector<double>> face_map;

    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        K[i] = k;
        A[i].resize(k);
        for (int j = 0; j < k; ++j) {
            cin >> A[i][j];
            if (face_map.find(A[i][j]) != face_map.end()) {
                face_map[A[i][j]][i] += 1;
            } else {
                face_map[A[i][j]] = vector<double>(n, 0);
                face_map[A[i][j]][i] += 1;
            }
        }
    }

    vector<vector<double>> face_p;

    for (auto& pair : face_map) {
        for (int k = 0; k < n; ++k) {
            pair.second[k] = pair.second[k] / K[k];
        }
        face_p.push_back(pair.second);
    }

    double result = -1;

    auto get_same_face_p = [&](const vector<vector<double>>& face_p, int i, int j) {
        double same_face_p = 0;
        for (const auto& fp : face_p) {
            if (fp[i] == 0 || fp[j] == 0) {
                continue;
            }
            same_face_p += fp[i] * fp[j];
        }
        return same_face_p;
    };

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double same_face_p = get_same_face_p(face_p, i, j);
            if (result < same_face_p) {
                result = same_face_p;
            }
        }
    }

    cout << setprecision(12) << result << endl;

    return 0;
}