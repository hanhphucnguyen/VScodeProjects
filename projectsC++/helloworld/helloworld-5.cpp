#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>

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

// Complete the howManyGames function below.
int howManyGames(int p, int d, int m, int s)
{
    int curPrice = p;
    int count = 0;
    while (s > 0)
    {
        s -= curPrice;
        if (s < 0)
            break;
        else
        {
            count++;
            curPrice -= d;
            if (curPrice < m)
                curPrice = m;
        }
    }
    return count;
}

// Complete the minimumDistances function below.
int minimumDistances(vector<int> a)
{
    int result = 0;
    int min = 0;
    for (int i = 0; i < a.size(); i++)
    {
        for (int j = i + 1; j < a.size(); j++)
        {
            if (a[i] == a[j])
            {
                min = abs(i - j);
                if (result == 0 || result > min)
                    result = min;
            }
        }
    }
    if (min == 0)
        return -1;
    else
    {
        return result;
    }
}

// Complete the kaprekarNumbers function below.
void kaprekarNumbers(int p, int q)
{
    vector<int> v;
    long int temp;
    int temp1, temp2;
    stringstream iss;
    char c;
    string s, s1, s2;
    for (int i = p; i <= q; i++)
    {
        if (i == 1)
            v.push_back(1);
        else
        {
            s = "";
            s1 = "";
            s2 = "";
            temp = (long int)i * i;
            iss.clear();
            iss << temp;
            while (iss >> c)
            {
                s += c;
            }
            for (int j = 0; j < s.size(); j++)
            {
                j < s.size() / 2 ? s1 += s[j] : s2 += s[j];
            }
            iss.clear();
            iss << s1;
            iss >> temp1;
            iss.clear();
            iss << s2;
            iss >> temp2;
            if (temp1 + temp2 == i)
                v.push_back(i);
        }
    }

    if (v.size() == 0)
        cout << "INVALID RANGE" << endl;
    else
    {
        for (int i : v)
        {
            cout << i << ' ';
        }
    }
}

// Complete the beautifulTriplets function below.
int beautifulTriplets(int d, vector<int> arr)
{
    int  count=0;
    if (arr.size()==1) return 0; else
    {
        for (int i = 0; i < arr.size() - 2; i++)
    {
        for (int j = i + 1; j < arr.size(); j++)
        {
            if (arr[i] == arr[j] - d)
            {
                for (int k = j + 1; k < arr.size(); k++)
                {
                    if (arr[j] == arr[k] - d)
                      count++;
                }
            }
        }
    }
    return count;
    }   
}

int main()
{
    vector<int> v{1, 2 ,4, 5, 7, 8, 10};
    // cout << repeatedString("a", 10) << endl;
    // vector<string> c{"10101","11100","11010","00101"};
    // vector<int> result = acmTeam(c);
    // vector<int> result = stones(3,1,2);
    // cout<<howManyGames(20,3,6,85);
    // cout << minimumDistances(v);
    // kaprekarNumbers(77778,77778);
    // cout<<beautifulTriplets(3,v);
    return 0;
}