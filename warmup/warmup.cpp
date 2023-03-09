#include <iostream>
#include <vector>
#include <stdlib.h>
#define int int
using namespace std;


// struct point
// {
//     int x, y;
// };

int32_t main(){
    int n, k, petya_row, petya_col;
    cin >> n >> k >> petya_row >> petya_col;
    petya_row--;
    petya_col--;
    if (n < k){
        cout << -1 << endl;
        return 0;
    }
    vector<vector<int>> matr((n+1)/2, {0, 0});
    // for (int i = 0; i < (n+1)/2; ++i){
    //     // cout << matr[i][0] << " " << matr[i][1] << endl; 
    // }
    int var, c;
    var = 1;
    c = 0;
    for (int i = 0; i < (n+1)/2; ++i){
        if (c == n){
            break;
        }
        else{
            matr[i][0] = var;
            var += 1;
            var = max(1, var % (k+1));
            c += 1;
            if (c == n){
                break;
            }
            matr[i][1] = var;
            var += 1;
            var = max(1, var % (k+1));
            c += 1;
        }
    }
    int pet_var = matr[petya_row][petya_col];
    vector<int> res = {1 << 30, 1 << 30};
    for (int i = 0; i < matr.size(); ++i){
        for (int j = 0; j < 2; ++j){
            if (matr[i][j] == pet_var && i != petya_row){
                if (abs(res[0] - petya_row) >= abs(i - petya_row)){
                    res = {i, j};
                }
            }
        }
    }
    if (res[0] < 1 << 30){
        cout << res[0] + 1 << " " << res[1] + 1<< endl;
    }
    else{
        cout << -1 << endl;
    }
    return 0;
}