// http://codeforces.com/contest/59/problem/A

#include <iostream>
using namespace std;

int main() {
	
	int i=0, u=0, l=0;
	string s;
	
	cin >> s;
	
	while(s[i]){
		if(islower(s[i])) l++;
		else u++;
		i++;
	}
	i=0;
	if(u > l){
		while(s[i]){
			if(islower(s[i])) cout << char(s[i]-32);
			else cout << s[i];
			i++;
		}
	}
	
	if(l >  u || l == u){
		while(s[i]){
			if(isupper(s[i])) cout << char(s[i]+32);
			else cout << s[i];
			i++;
		}
	}
	
	return 0;
}