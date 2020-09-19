#include <bits/stdc++.h>
using namespace std;

int arr[] = {1, 2, 5, 10, 20, 50, 100, 500, 1000};

void minimumCoinsGP(int V){
	int n = sizeof(arr)/sizeof(arr[0]);
	// step 1 : sorting
	sort(arr, arr+n);
	// step 2: init an vector
	vector<int> result;
	// iterate through the coins array(from largest to smallest)
	for(int i=n-1; i>=0; i--){
		// find largest denomination, keep adding until it becomes > 0
		while(V >= arr[i]){
			V -= arr[i];
			result.push_back(arr[i]);
		}
	}
	for(auto x: result) cout << x << " ";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int V; cin >> V;
	
	minimumCoinsGP(V);
	
	return 0;
}