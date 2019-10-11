#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

// Complete the designerPdfViewer function below.
int designerPdfViewer(vector<int> h, string word)
{
    int s = word.size();
    int max;
    vector<int> wordSize;

    for (int i = 0; i < s; i++)
    {
        char temp = word[i];
        wordSize.push_back(int(temp) - 97);
    }
    max = h[wordSize[0]];

    for (int i = 0; i < s; i++)
    {
        if (max < h[wordSize[i]])
            max = h[wordSize[i]];
    }

    return max * s;
}

int utopianTree(int n)
{
    int result = 0;
    for (int i = 0; i <= n; i++)
    {
        if (i % 2 == 0)
            result++;
        else
            result *= 2;
    }
    return result;
}

string angryProfessor(int k, vector<int> a)
{
    int count = 0;
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] <= 0)
            count++;
    }
    if (count >= k)
        return "NO";
    else
        return "YES";
}

// Complete the beautifulDays function below.
int beautifulDays(int i, int j, int k)
{
    string str, ret;
    int count = 0;
    int tempNum;
    for (int t = i; t <= j; t++)
    {
        ret = "";
        str = to_string(t);
        for (int k = str.size() - 1; k >= 0; k--)
        {
            ret += str[k];
        }
        stringstream iss(ret);
        iss >> tempNum;
        if ((t - tempNum) % k == 0)
            count++;
    }
    return count;
}

// Complete the viralAdvertising function below.
int viralAdvertising(int n)
{
    vector<int> v1, v2, v3;
    for (int i = 0; i < n; i++)
    {
        i == 0 ? v1.push_back(5) : v1.push_back(v2[i - 1] * 3);
        v2.push_back(v1[i] / 2);
        i == 0 ? v3.push_back(v2[0]) : v3.push_back(v3[i - 1] + v2[i]);
    }
    return v3[v3.size() - 1];
}

int main()
{
    // vector<int> v{1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7};
    cout << viralAdvertising(3);
    return 0;
}