#include <iostream>
#include <vector>
#include <string>

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
    int count=0;
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i]<=0) count++;
    }
    if (count >= k)
        return "NO";
    else
        return "YES";
}

int main()
{
    // vector<int> v{1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7};
    // cout<<dayOfProgrammer(2016);
    // cout << designerPdfViewer(v, "zaba");
    return 0;
}