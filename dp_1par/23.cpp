#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    if (n == 1){
        cout << 0 << '\n' << 1 << endl;
        return 0;
    }else if (n == 2){
        cout << 1 << '\n' << 1 << '\n' << 2 << endl;
    }else if (n == 3){
        cout << 1 << '\n' << 1 << '\n' << 3 << endl;
    }
    vector<int> dp(n);
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 1;
    vector<int> path;
    path.push_back(1);
    for (int i = 3; i < n; ++i){
        int min_dp = 1 << 15;
        if ((i+1) % 2 == 0){
            min_dp = min(min_dp, dp[i/2]);
        }
        if ((i+1) % 3 == 0){
            min_dp = min(min_dp, dp[i/3]);
        }
        min_dp = min(min_dp, dp[i-1]);
        if (min_dp == dp[i/2] and (i+1) % 2 == 0){
            path.push_back((i+1)/2);
        }
        else if (min_dp == dp[i/3] and (i+1) % 3 == 0){
            path.push_back((i+1)/3);
        }
        else{
            path.push_back(i);
        }
        dp[i] = min_dp + 1;
    }
    cout << dp[n-1] << endl;
    for (int i : path){
        cout << i << ' ';
    }
    cout << n << endl;
    return 0;
}