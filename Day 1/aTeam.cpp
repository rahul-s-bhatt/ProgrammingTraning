//http://codeforces.com/contest/231/problem/A
#include <iostream>
using namespace std;

int main() {
	int t, i, j, c=0, countMax=0; 
	cin >> t;
	int arr[t][t];
	for(i=0; i<t; i++){
		for(j=0; j<3; j++){
			cin >> arr[i][j];
			if(arr[i][j] == 1) c++;
		}
		if(c >= 2) countMax++;
		c = 0;
	}
	cout << countMax;
	return 0;
}