// http://codeforces.com/contest/268/problem/A
// https://ideone.com/CRWKSx

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	vector<int> v1, v2;
	
	int a, b, count=0;
	
	for(int i=0; i<t; i++){
		cin >> a >> b;
		v1.push_back(a);
		v2.push_back(b);
	}
	
	for(int i=0; i<t; i++)
		for(int j=0; j<t; j++)
			if(v1[i]==v2[j]) count++;
	cout << count;
	
	return 0;
}