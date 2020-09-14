#include<bits/stdc++.h>
#include <unordered_map>
#define endl "\n"
using namespace std;

int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int arr[5] = {1, 2, 2, 1, 4};
    unordered_map<int, int> mp;

    for(int i=0; i<5; i++) mp[arr[i]];

    for(int i=0; i<5; i++) cout << mp.first << " " << mp.second << endl;

    return 0;
}