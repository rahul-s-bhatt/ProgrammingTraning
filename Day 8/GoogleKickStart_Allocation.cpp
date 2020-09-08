#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int t;
	cin >> t;
	
	int temp = 1;
	
	int n, b;
	
	for(int i=0; i<t; i++){
		cin >> n >> b;
		int arr[n];
		
		for(int j=0; j<n; j++) cin >> arr[j];
		sort(arr, arr+n);
		int count=0;
		for(int j=0; j<n; j++){
			if(b >= arr[j]){
				b -= arr[j];
				++count;
			}
		}
		cout << "Case #" << temp++  << ": " << count <<endl;
	}
	
	return 0;
}