#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <deque>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;


int main()
{
    vector<int> v{1, 2, 3, 3, 3, 4, 4, 4, 5};
    
    //vector
    // bool a = binary_search(v.begin(),v.end(),1);
    // sort(v.begin(),v.end());
    // vector<int>::iterator it = lower_bound(v.begin(),v.end(),3);  //>=
    // vector<int>::iterator it2 = upper_bound(v.begin(),v.end(),4); //>
    // cout<< *it<<endl;
    // cout<< *it2<<endl;
    // cout<< it2 - it<<endl;

    //set
    // set<int> set;
    // set.insert(5);
    // set.insert(4);
    // set.insert(3);
    // set.insert(2);

    // auto it = set.find(5);
    // cout << *it << endl;

    // auto it2 = set.lower_bound(4);
    // auto it3 = set.lower_bound(6);
    // if (it3 == set.end())
    //     cout << "can not find that number" << endl;
    // set.erase(4);
    // for (int x : set)
    // {
    //     cout << x << " ";
    // }

    //map
    map<int, int> m;
    m[0] = 1;
    m[10] = 23;
    map<char,int> map2;
    string temp = "fdsgfdghdfbhfdaaa";
    cout<< m[0]<<endl;
    for(char x:temp)
    {
        map2[x]++;
    }
    cout<<map2['a']<<endl;

    return 0;
}