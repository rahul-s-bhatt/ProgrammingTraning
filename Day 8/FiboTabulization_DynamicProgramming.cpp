#include <bits/stdc++.h>
#define NIL -1
#define MAX 100

using namespace std;

int fibTablu(int n){
	int f[n+1];
	int i;
	f[0] = 0; f[1] = 1;
	
	for(i=2; i<=n; i++) f[i] = f[i-1] + f[i-2];
	return f[n];
}

int main() {
	
	int n = 40;
	
	cout << fibTablu(n);
	
	return 0;
}