// http://codeforces.com/contest/263/problem/A

#include <iostream>
using namespace std;

int main() {
	
	int indexOfOneCol, indexOfOneRow;
	int arr[5][5];
	
	for(int i=0; i<5; i++){
		for(int j=0; j<5; j++){
			cin >> arr[i][j];
			if(arr[i][j] == 1){indexOfOneRow = i+1; indexOfOneCol = j+1;}
		}
	}
	cout << (abs(indexOfOneRow-3) + abs(indexOfOneCol-3));
	return 0;
}