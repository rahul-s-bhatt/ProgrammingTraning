#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int t; cin >> t;
	
	while(t--){
		string s;
		cin >> s;
		
		int lFreq[26], rFreq[26];
		for(int i=0; i<26; i++){
			lFreq[i] = 0;
			rFreq[i] = 0;
		}
		
		for(int i=0; i<s.length()/2; i++){
			lFreq[s[i] - 'a']++;
		}
		
		for(int j=(s.length()+1)/2; j<s.length(); j++){
			rFreq[s[j] - 'a']++;
		}
		
		bool isSame = true;
		
		for(int i=0; i<26; i++){
			if(lFreq[i] != rFreq[i]){
				isSame = false;
				break;
			}
		}
		
		if(isSame){
			cout << "YES\n";
		}else{
			cout << "NO\n";
		}
		
		
	}
	
	return 0;
}