#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

 
// Group anagrams together from given array of words
vector<vector<string> > groupAnagrams(vector<string> input_list)
{
    // the first value will hold the sorted word as key, the second vector is used to hold the multiple values.
    unordered_map<string, vector<string> > my_map;
    vector<vector<string> > final_list; //vector to hold all the element after sorting
 
    for (int i = 0; i < input_list.size(); i++)
    {
        // take value at the index as a key and sort it further
        string key = input_list[i];
 
        //sort the key
        sort(key.begin(), key.end());
 
        // add the value to that key
        my_map[key].push_back(input_list[i]);
 
    }
 
    for (auto n : my_map)
    {
        // copy  all the values from the map to the vector of strings
        final_list.push_back(n.second);
    }
 
    return final_list;
}
 
 
//Main driver function
int main()
{
    vector<string> anagram_set;
    anagram_set.push_back("cat");
    anagram_set.push_back("bat");
    anagram_set.push_back("tac");
    anagram_set.push_back("eat");
    anagram_set.push_back("tab");
    anagram_set.push_back("ate");
     
    vector<vector<string> > print_set =  groupAnagrams(anagram_set);
 
    // print the output
    for (int i = 0; i < print_set.size(); i++)
    {
        if (print_set[i].size() > 0)
        {
            cout << " ( ";
            for (int j = 0; j < print_set[i].size(); j++)
                cout << print_set[i][j] << " ";
            cout << ")";
        }
        cout<<endl;
    }
 
    return 0;
}