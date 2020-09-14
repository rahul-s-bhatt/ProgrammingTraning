#include <bits/stdc++.h>
using namespace std;

int coinChange(int S[], int m, int n){
    if(n == 0) return 1;
    if(n < 0) return 0;
    if(m <=0 && n >= 1) return 0;
     // count is sum of solutions 
    //  (i) including S[m-1]
    // (ii) excluding S[m-1] 
    return coinChange(S, m-1, n) + coinChange(S, m, n-S[m-1]); 
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int arr[3] = {1, 2, 3};
    int m = 3;
    cout << coinChange(arr, m, 4);


    return 0;
}