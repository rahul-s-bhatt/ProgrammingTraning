#include bitsstdc++.h
using namespace std;

int binominalCoefficient(int n, int k){
	if(k == 0  k == n) return 1;
	return binominalCoefficient(n-1, k) + binominalCoefficient(n-1, k-1);
}

int main() {
	
	ios_basesync_with_stdio(false);
	cin.tie(NULL);
	
	int n=5, k = 2;
	cout  binominalCoefficient(n, k);
	
	return 0;
}