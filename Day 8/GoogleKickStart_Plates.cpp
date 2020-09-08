#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	int temp = 1;
	
	while(t--){
		
		int n, k, p, sum;
		cin >> n >> k >> p;
		
		int size = k*n;
		int arr[size];
			
		// cout << size << endl;
		
		for(int i=0; i<size; i++) cin >> arr[i];
		
		// for(int i=0; i<size; i++) cout << arr[i] <<endl;
		
		sum=0;
		for(int i=0; i<k && p > 0; i++){
			sum += max(arr[i], arr[i+n-1]);
			p--;
		};
		cout << "Case #" << temp++ <<": " << sum << endl;
	}
	
	return 0;
}