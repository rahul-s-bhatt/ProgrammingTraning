#include <bits/stdc++.h>
using namespace std;

int binominalCoefficient(int n, int k){
	
	int dp[k+1];
	
	memset(dp, 0, sizeof(dp));
	
	dp[0] = 1; //nC0 is 1
	
	for(int i=1; i<=n; i++){
		for(int j=min(i, k); j>0;j--){
			dp[j] = dp[j] + dp[j-1];
		}
	}
	
	return dp[k];
}

int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n=5, k = 2;
	cout << binominalCoefficient(n, k);
	
	return 0;
}