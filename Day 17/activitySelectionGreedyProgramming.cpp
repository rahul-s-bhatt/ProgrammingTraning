#include <bits/stdc++.h>
using namespace std;

void activitySelection(int start[], int finish[], int n){
	int i, j=0;
	for(int i=1; i<n; i++){
		if(start[i] >= finish[j]){
			cout << i << " ";
			j=i;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n; cin >> n;
	int start[n], finish[n];
	
	for(int i=0; i<n; i++) cin >> start[i];
	for(int i=0; i<n; i++) cin >> finish[i];
	
	activitySelection(start, finish, n);
	return 0;
}