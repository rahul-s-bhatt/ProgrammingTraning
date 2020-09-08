#include <bits/stdc++.h>
#define NIL -1
#define MAX 100

using namespace std;

int lookup[MAX];

void _init(){
	for(int i=0; i<MAX; i++) lookup[i] = NIL;
}

int fibMemo(int n){
	if(lookup[n] == NIL){
		if(n <=1) lookup[n] = n;
		else lookup[n] = fibMemo(n-1) + fibMemo(n-2);
	}
	return lookup[n];
}

int main() {
	
	int n = 5;
	_init();
	
	cout << fibMemo(n);
	
	return 0;
}