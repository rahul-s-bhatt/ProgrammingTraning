#include <iostream>
using namespace std;

int main() {
	int a, b;
	string dieRoll[6] = {"1/6", "1/3", "1/2", "2/3", "5/6", "1/1"};
	 cin >> a >> b;
	 
	 int max = (a > b) ? a : b;
	 
	 cout << dieRoll[6-max];
	 
	return 0;
}