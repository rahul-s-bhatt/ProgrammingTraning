// http://codeforces.com/contest/381/problem/A
// https://ideone.com/41UfgS

#include <iostream>
using namespace std;

int main() {
	int t, count = 1;
	cin >> t;
	int arr[t];
	
	for(int i=0; i<t; i++) cin >> arr[i];
	
	int sereja=0, dima=0, f=0, e=t-1;
	char turn = 's';
	
	while(f != e){
		if(arr[f] > arr[e] && turn == 's'){ sereja += arr[f++];  turn = 'd';}
		else if (arr[f] > arr[e] && turn == 'd'){dima += arr[f++]; turn='s';}
		else if(arr[f] < arr[e] && turn == 's'){ sereja += arr[e--];  turn = 'd';}
		else if (arr[f] < arr[e] && turn == 'd'){dima += arr[e--]; turn='s';}
	}
	
	if(f == e && (turn == 'd')) dima += arr[f++];
	if(f == e && (turn == 's')) sereja += arr[f++];
	
	cout << sereja << " " << dima;
	
	return 0;
}