#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

vector<vector<int>> multiply(vector<vector<int>> mat1, vector<vector<int>> mat2) {
    // mat1, mat2 : 2 by 2 matrices
    int s1 = mat1[1][0] + mat1[1][1];
    int s2 = s1 - mat1[0][0];
    int s3 = mat2[0][1]-mat2[0][0];
    int s4 = mat2[1][1] - s3;
    int m2 = mat1[0][0] * mat2[0][0];
    int m5 = s1*s3;
    int t1 = s2*s4+m2;
    int t2 = t1+(mat1[0][0]-mat1[1][0])*(mat2[1][1]-mat2[0][1]);
    return {{m2+mat1[0][1] * mat2[1][0], t1+m5+(mat1[0][1]-s2)*mat2[1][1]},{t2-mat1[1][1]*(s4-mat2[1][0]), t2+m5}};
}

vector<vector<int>> matadd(vector<vector<int>> A, vector<vector<int>> B, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] += B[i][j];
        }
    }
    return A;
}

std::vector<std::vector<int>> matadd_c(std::vector<std::vector<int>> A, int constant, int N) {
    for (int i = 0; i < N; i++) {
      A[i][i] += constant;
    }
    return A;
}

vector<vector<int>> matsub(vector<vector<int>> A, vector<vector<int>> B, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] -= B[i][j];
        }
    }
    return A;
}

vector<vector<int>> strassen_mul(const vector<vector<int>> A, vector<vector<int>> B, int N) {
    if (N == 2) {
        return multiply(A, B);
    }
    int n = N/2;
    vector<vector<int>> A11(n, vector<int>(n)), A12(n, vector<int>(n)), A21(n, vector<int>(n)), A22(n, vector<int>(n));
    vector<vector<int>> B11(n, vector<int>(n)), B12(n, vector<int>(n)), B21(n, vector<int>(n)), B22(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j+n];
            A21[i][j] = A[i+n][j];
            A22[i][j] = A[i+n][j+n];
            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j+n];
            B21[i][j] = B[i+n][j];
            B22[i][j] = B[i+n][j+n];
        }
    }
    vector<vector<int>> S1 = matadd(A21, A22, n);
    vector<vector<int>> S2 = matsub(S1, A11, n);
    vector<vector<int>> S3 = matsub(B12, B11, n);
    vector<vector<int>> S4 = matsub(B22, S3, n);
    vector<vector<int>> M1 = strassen_mul(S2, S4, n);
    vector<vector<int>> M2 = strassen_mul(A11, B11, n);
    vector<vector<int>> M3 = strassen_mul(A12, B21, n);
    vector<vector<int>> M4 = strassen_mul(matsub(A11, A21, n), matsub(B22, B12, n), n);
    vector<vector<int>> M5 = strassen_mul(S1, S3, n);
    vector<vector<int>> M6 = strassen_mul(matsub(A12, S2, n), B22, n);
    vector<vector<int>> M7 = strassen_mul(A22, matsub(S4, B21, n), n);
    vector<vector<int>> T1 = matadd(M1, M2, n);
    vector<vector<int>> T2 = matadd(T1, M4, n);
    vector<vector<int>> C11 = matadd(M2, M3, n);
    vector<vector<int>> C12 = matadd(T1, matadd(M5, M6, n), n);
    vector<vector<int>> C21 = matsub(T2, M7, n);
    vector<vector<int>> C22 = matadd(T2, M5, n);
    vector<vector<int>> res(N, vector<int>(N));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            res[i][j] = C11[i][j];
            res[i][j+n] = C12[i][j];
            res[i+n][j] = C21[i][j];
            res[i+n][j+n] = C22[i][j];
        }
    }
    return res;
}

int mattr(vector<vector<int>> mat, int N) {
    int trace = 0;
    for (int i = 0; i < N; i++) {
        trace += mat[i][i];
    }
    return trace;
}

vector<int> charpoly(vector<vector<int>> A, int original_size, int extended_size) {
    vector<int> c(original_size + 1, 0);
    c[0] = 1;
    vector<vector<int>> mat(extended_size, vector<int>(extended_size, 0)); // mat 변수의 형식을 vector<vector<int>>로 변경
    for (int i = 0; i < original_size; i++) {
        mat[i][i] = 1;
    }
    for (int k = 1; k <= original_size; k++) {
        if (k > 1) {
            mat = strassen_mul(A, matadd_c(mat, c[k - 1], original_size), extended_size);
        }
        int tr = mattr(mat, original_size);
        c[k] = -tr / k;
    }
    return c;
}

int main() {
    int n, M;
    cin >> n >> M;

    vector<vector<int>> A(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];
        }
    }
    int k2 = 1;
    while (k2 < n) {
        k2 *= 2;
    }
    vector<vector<int>> B(k2, vector<int>(k2));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            B[i][j] = A[i][j];
        }
    }

    vector<int> poly = charpoly(B, n, k2);

    for (int i = n; i >= 0; i--) {
        int c_i = poly[i];
        cout << c_i % M << endl;
    }

    return 0;
}


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> charpoly(const vector<vector<int>>& A) {
    int n = A.size();
    vector<int> poly(2*n+1, 0);
    poly[2*n] = 1;
    vector<vector<int>> rows(n, vector<int>(n+1));
    for (int i = 0; i < n; i++) {
        rows[i] = vector<int>(A[i].begin(), A[i].end());
        rows[i].push_back(poly[n+i]);
    }
    for (int i = n-1; i >= 0; i--) {
        int d = rows[i][i];
        if (d == 0) continue; // 예외 처리
        for (int j = i+1; j < n; j++) {
            int c = rows[j][i] / d;
            for (int k = i; k < n+1; k++) {
                rows[j][k] -= c * rows[i][k];
            }
        }
        poly[n+i] = -rows[i][n] / d;
    }
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        result[i] = poly[n+i+1];
    }
    return result;
}
int main() {
    int n, M;
    cin >> n >> M;

    vector<vector<int>> C(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> C[i][j];
        }
    }

    vector<int> poly = charpoly(C);

    for (int i = 0; i < poly.size(); i++) {
        std::cout << poly[i] << std::endl;
    }

    for (int i = n; i >= 0; i--) { // i의 초기값을 n-1로 변경
        int c_i = poly[i];
        if (c_i < 0) {
            c_i = M-(-c_i)%M
        }
        std::cout << c_i % M << std::endl;
    }

    return 0;
}


#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> string_to_poly(const string& s) {
    vector<int> poly;
    int i = 0;
    while (i < s.length()) {
        int j = i;
        while (j < s.length() && s[j] >= '0' && s[j] <= '9') {
            j++;
        }
        int coef = stoi(s.substr(i, j-i));
        if (coef != 0) {
            int exp = s.length() - j;
            if (exp == 0) {
                poly.push_back(coef);
            } else {
                while (poly.size() < exp) {
                    poly.push_back(0);
                }
                poly.push_back(coef);
            }
        }
        i = j+1;
    }
    reverse(poly.begin(), poly.end());
    return poly;
}
vector<int> charpoly(const vector<vector<int>>& A) {
    int n = A.size();
    vector<int> poly(2*n+1, 0);
    poly[2*n] = 1;
    vector<vector<int>> rows(n, vector<int>(n+1));
    for (int i = 0; i < n; i++) {
        rows[i] = vector<int>(A[i].begin(), A[i].end());
        rows[i].push_back(poly[n+i]);
    }
    for (int i = n-1; i >= 0; i--) {
        int d = rows[i][i];
        if (d == 0) continue; // 예외 처리
        for (int j = i+1; j < n; j++) {
            int c = rows[j][i] / d;
            for (int k = i; k < n+1; k++) {
                rows[j][k] -= c * rows[i][k];
            }
        }
        poly[n+i] = -rows[i][n-1] / d;
    }
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        result[i] = poly[n+i+1];
    }
    return result;
}
int main() {
    int n, M;
    cin >> n >> M;

    vector<vector<int>> C(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        vector<int> poly = string_to_poly(s);
        for (int j = 0; j < n; j++) {
            C[i][j] = poly[j];
        }
    }

    vector<int> poly = charpoly(C);

    for (int i = n; i >= 0; i--) { // 변경: 초기값을 n-1로 설정
        int c_i = poly[i];
        if (c_i < 0) {
            c_i = M-(-c_i)%M;
        }
        std::cout << c_i % M << std::endl;
    }

    return 0;
}