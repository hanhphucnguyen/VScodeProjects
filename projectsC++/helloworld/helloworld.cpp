#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <deque>

using namespace std;

// Complete the jumpingOnClouds function below.
int jumpingOnClouds(vector<int> c, int k)
{
    int count = 100;
    int i = 0;
    do
    {
        count--;
        if (c[i] == 1)
            count -= 2;
        i += k;
    } while (i < c.size());

    return count;
}

// Complete the appendAndDelete function below.
string appendAndDelete(string s, string t, int k)
{

    int commonLength = 0;
    int minlength;
    s.size() >= t.size() ? minlength = t.size() : minlength = s.size();

    for (int i = 0; i < minlength; i++)
    {
        if (s[i] == t[i])
            commonLength++;
        else
            break;
    }

    if ((s.length() + t.length() - 2 * commonLength) > k)
    {
        return "No";
    }

    else if ((s.length() + t.length() - 2 * commonLength)  <= k )
    {
        return "Yes";
    }

    else
    {
        return "No";
    }
}

int main()
{
    // vector<int> v{0, 0, 1, 0, 0, 1, 1, 0};
    // cout << jumpingOnClouds(v, 2) << endl;
    // cout<<appendAndDelete("abc","abc",7);
    return 0;
}