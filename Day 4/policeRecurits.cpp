// http://codeforces.com/contest/427/problem/A
// https://ideone.com/1dZUu1

#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	int arr[t];
	for(int i=0;i<t;i++) cin >> arr[i];
	
	int count=0, ar=0;
	
	for(int i=0; i<t; i++){
		if(arr[i] != -1 && ar>=0) ar += arr[i];
		else if(arr[i] == -1 && ar!=0) ar--;
		else if(arr[i] == -1 && ar==0) count++;
	}
	cout << count;
	return 0;
}