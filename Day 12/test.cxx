#include<bits/stdc++.h>
#include <unordered_map>
#define endl "\n"
using namespace std;

int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // Declaring umap to be of <string, int> type 
    // key will be of string type and mapped value will 
    // be of double type 
    unordered_map<string, int> umap; 
  
    // inserting values by using [] operator 
    umap["GeeksforGeeks"] = 10; 
    umap["Practice"] = 20; 
    umap["Contribute"] = 30; 
  
    // Traversing an unordered map 
    for (auto x : umap) 
      cout << x.first << " " << x.second << endl; 
  
} 