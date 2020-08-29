// http://codeforces.com/contest/344/problem/A
// https://ideone.com/scI9Ge
#include <iostream>
using namespace std;

int main() {
	int t, count = 1;
	cin >> t;
	int arr[t];
	
	for(int i=0; i<t; i++) cin >> arr[i];
	
	for(int i=0; i<t-1; i++){
		if(arr[i] != arr[i+1]) count++;
	}
	
	cout << count;
	
	return 0;
}