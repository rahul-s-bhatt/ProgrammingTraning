// http://codeforces.com/contest/680/problem/B
#include <iostream>
using namespace std;

int main() {
	int t, k;
	cin >> t >> k;
	int arr[t];
	
	for(int i=0; i<t; i++) cin >> arr[i];
	
	int count=0, i=k-1, j=k+1;
	
	while(i >= 0 && j < t){
		if(arr[i] == 1 && arr[j] == 1) count+=2;
		i--;
		j++;
	}
	
	i=k-1, j=k+1;
	if(count == 0){
		while(arr[i] == 1 && i >= 0){ if(arr[i] == 1){count++; i--;} }
		while(arr[j] == 1 && j < t){ if(arr[j] == 1){count++; j++;} }
	
		cout << count;
	} else {
		cout << count+1;
	}
	
	return 0;
}