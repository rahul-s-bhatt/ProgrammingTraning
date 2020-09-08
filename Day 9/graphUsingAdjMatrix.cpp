#include<bits/stdc++.h>
#define MAX 1001
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int matrix[MAX][MAX];

    int i, m, n, q, a, b;

    cin >> n >> m;

    for(i=1; i<=m; i++){
        cin >> a >> b;
        matrix[a][b] = 1;
        matrix[b][a] = 1;
    }

    cin >> q;
    for(i=1; i<=m; i++){
        if(matrix[a][b] == 1) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}