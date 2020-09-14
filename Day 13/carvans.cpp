#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t; cin >> t;
	
	while(t--){
		int n; cin >> n;
		int arr[n];
		
		for(int i=0; i<n; i++) cin >> arr[i];
		
		int ans=0;
		int prevCarSpeed = INT_MAX;
		
		for(int i=0; i<n; i++){
			if(prevCarSpeed >= arr[i]){
				ans++;
				prevCarSpeed = arr[i];
			}
		}
		
		cout << ans << "\n";
	}
	
	return 0;
}