#include <bits/stdc++.h>
using namespace std;

void print(unordered_map<string, vector<string>>& store){
	unordered_map<string, vector<string>> ::iterator it;
	for(it = store.begin(); it != store.end(); it++){
		vector<string> tempVec(it->second);
		int size = tempVec.size();
		if(size > 1){
			for(int i=0; i<size; i++){
				cout << tempVec[i] << " ";
			}
			cout << "\n";
		}
	}
}

void storeItInMap(vector<string>& vec){
	unordered_map< string, vector<string> > store;
	
	for(int i=0; i<vec.size(); i++){
		string tempString(vec[i]);
		sort(tempString.begin(), tempString.end());
		
		if(store.find(tempString) == store.end()){
			vector<string> tempVector;
			tempVector.push_back(vec[i]);
			store.insert(make_pair(tempString, tempVector));
		}
		else{
			vector<string> tempVector;
			tempVector.push_back(vec[i]);
			store[tempString] = tempVector;
		}
		
	}
	print(store);
}

int main() {
	vector<string> arr;
	arr.push_back("geeksquiz"); 
    arr.push_back("geeksforgeeks"); 
    arr.push_back("abcd"); 
    arr.push_back("forgeeksgeeks"); 
    arr.push_back("zuiqkeegs"); 
    arr.push_back("cat"); 
    arr.push_back("act"); 
    arr.push_back("tca"); 
	
	storeItInMap(arr);
	return 0;
}