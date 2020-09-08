// http://codeforces.com/contest/731/problem/A?mobile=false
// https://ideone.com/0tGzsc

#include <iostream>
using namespace std;

int main() {
	string s;
	cin >> s;
	
	int sum = s[0] > 'a' ? min(26 + 'a'-s[0], s[0] - 'a') : abs('a' - s[0]);

	for(int i=1; i<s.length(); i++){
		sum += s[i-1] > s[i] ? min(26 + s[i] - s[i-1], s[i-1]-s[i]) : min(s[i] - s[i-1], 26 + s[i-1] - s[i]);
	}
	
	cout << sum;
	return 0;
}