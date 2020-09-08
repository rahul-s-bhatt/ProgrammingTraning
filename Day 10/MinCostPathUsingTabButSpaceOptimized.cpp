#include<bits/stdc++.h>
#define endl "\n"
using namespace std;

const int row = 3;
const int col = 3;

int minCost(int cost[row][col]){
    
    // first col
    for(int i=1; i<row; i++)
        cost[i][0] += cost[i-1][0];
    
    // first row 
    for(int j=1; j<col; j++)
        cost[0][j] += cost[0][j-1];
    
    // rest of the 2d matrix
    for(int i=1; i<row; i++)
        for(int j=1; j<col; j++)
            cost[i][j] += min(cost[i-1][j-1], min(cost[i-1][j], cost[i][j-1]));        

    // returning last value
    return cost[row-1][col-1];
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int cost[row][col] = {  {1, 2, 3},  
                              {4, 8, 2},  
                              {1, 5, 3} }; 
  
    cout << minCost(cost) << endl; 

    return 0;
}