#include<bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<int> v[10];

    int i, n, m, a, b;

    cin >> n >> m;
    for(i=0; i<m; i++){
        cin >> a >> b;
        v[a].push_back(b);
    }

    for(i=1; i<=n; ++i){
        for(int j=0; j<v[i].size(); j++){
            if(j==v[i].size()-1) cout << v[i][j] << "\n";
            else cout << v[i][j] << "-->";
        }
    }

    return 0;
}