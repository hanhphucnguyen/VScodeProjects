#include <iostream>
#include <vector>
#include <string>
#include <set>

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

vector<int> acmTeam(vector<string> topic)
{
    int maxTopic = 0;
    int topics;
    int numOfGroup = 0;
    int count = 0;
    for (int i = 0; i < topic.size(); i++)
    {
        for (int j = 0; j < topic.size(); j++)
        {
            if (i == j)
                continue;
            else
            {
                count = 0;
                for (int k = 0; k < topic[i].size(); k++)
                {
                    if (topic[i][k] == '1' || topic[j][k] == '1')
                        count++;
                }
                topics = count;
            }
            if (maxTopic < topics)
            {
                maxTopic = topics;
                numOfGroup = 1;
            }
            else
            {
                if (maxTopic == topics && i < j)
                    numOfGroup++;
            }
        }
    }
    vector<int> v;
    v.push_back(maxTopic);
    v.push_back(numOfGroup);
    return v;
}

// Complete the stones function below.
vector<int> stones(int n, int a, int b)
{
    set<int> st;
    vector<int> result;

    for (int i = 0; i < n; i++)
        st.insert(i * a + (n - 1 - i) * b);

    for (auto x : st)
    {
        result.push_back(x);
    }
    return result;
    // def stones(n, a, b):
    // return sorted(set([a*i+b*(n-1-i) for i in range(n)]))
}

int main()
{
    // vector<int> v{1, 2, 3, 1, 2, 3, 3, 3};
    // cout << repeatedString("a", 10) << endl;
    // vector<string> c{"10101","11100","11010","00101"};
    // vector<int> result = acmTeam(c);
    return 0;
}