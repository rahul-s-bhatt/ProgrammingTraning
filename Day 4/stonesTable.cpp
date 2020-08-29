// http://codeforces.com/contest/266/problem/A
// https://ideone.com/XpCj6s
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	string s;
	cin >> s;
	
	int count=0;
	for(int i=0; i<t-1; i++){
		if(s[i] == s[i+1]) count++; 
	}
	cout << count;
	return 0;
}