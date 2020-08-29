// http://codeforces.com/contest/344/problem/A
// https://ideone.com/bIz0OH

#include <iostream>
using namespace std;

int main() {
	int t, previousCount=0, currentCount=0;
	cin >> t;
	int arr[t];
	
	for(int i=0;i<t; i++) cin >> arr[i];
	
	for(int i=0; i<t-1; i++){
		if(arr[i] != arr[i+1]){
			previousCount = previousCount < currentCount ? currentCount : previousCount;
			currentCount = 0;
		}
		else currentCount++;
	}
	
	previousCount < currentCount?cout << currentCount+1: cout << previousCount+1;
	
	return 0;
}