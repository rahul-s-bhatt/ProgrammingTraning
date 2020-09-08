#include<bits/stdc++.h>
#define R 3
#define C 3

using namespace std;

int min(int x, int y, int z) 
{ 
   if (x < y) 
      return (x < z)? x : z; 
   else
      return (y < z)? y : z; 
} 

/* Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]*/
int minCost(int cost[R][C], int m, int n) 
{ 
   if (n < 0 || m < 0) 
      return INT_MAX; 
   else if (m == 0 && n == 0) 
      return cost[m][n]; 
   else
      return cost[m][n] + min( minCost(cost, m-1, n-1), 
                               minCost(cost, m-1, n),  
                               minCost(cost, m, n-1) ); 
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int cost[R][C] = { {1, 2, 3}, 
                      {4, 8, 2}, 
                      {1, 5, 3} }; 

    cout << minCost(cost, 2, 2);    

    return 0;
}