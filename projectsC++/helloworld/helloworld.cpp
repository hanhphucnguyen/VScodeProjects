#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n)
{
    int numOfa = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == 'a')
            numOfa++;
    }

    if (s.size() == 1 && numOfa == 1)
        return n;
    else if (n % s.size() == 0)
    {
        return n / s.size() * numOfa;
    }
    else
    {
        int remain;
        int result = 0;
        int cur = 0;
        remain = n % s.size();
        for (int i = 0; i < remain; i++)
        {
            if (s[cur] == 'a')
                result++;
            cur++;
        }
        return (n / s.size() * numOfa) + result;
    }
}

int main()
{
    // vector<int> v{1, 2, 3, 1, 2, 3, 3, 3};
    // cout << repeatedString("a", 10) << endl;
    return 0;
}