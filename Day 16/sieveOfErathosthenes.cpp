#include <bits/stdc++.h>
using namespace std;

void SieveOfErathosthenes(int n){
	// create bool array "prime"
	// all entries it as true. A value in prime[i]
	// will finally be false if i is Not a prime, else true.
	bool prime[n+1];
	memset(prime, true, sizeof(prime));
	
	for(int p=2; p*p<=n; p++){
		// if prime[p] is not changed, then it is a prime
		if(prime[p] == true){
			// update all multiples of p greater than or
			// equal to the square of it
			// numbers which are multiple of p and are
			// less than p^2 are already been marked.
			for(int i=p*p; i<=n; i+=p) prime[i] = false;
		}
	}
	for(int p=2; p<=n; p++){
		if(prime[p]) cout << p << " ";
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n = 30;
	SieveOfErathosthenes(n);
	
	return 0;
}