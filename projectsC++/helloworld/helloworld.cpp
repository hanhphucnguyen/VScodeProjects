#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

int getTotalX(vector<int> &a, vector<int> &b)
{
    int r1 = a[a.size() - 1];
    int r2 = b[0];
    int count = 0;
    bool flag1, flag2;

    for (int i = r1; i <= r2; i++)
    {
        flag1 = true;
        flag2 = true;
        for (int j = 0; j < a.size(); j++)
        {
            if (i % a[j] != 0)
            {
                flag1 = false;
                break;
            }
        }

        for (int j = 0; j < b.size(); j++)
        {
            if (b[j] % i != 0)
            {
                flag2 = false;
                break;
            }
        }
        if (flag1 && flag2)
            count++;
    }
    return count;
}

// Complete the breakingRecords function below.
vector<int> breakingRecords(vector<int> scores)
{
    vector<int> result{0, 0};
    int max = scores[0], min = scores[0];
    for (int i = 0; i < scores.size(); i++)
    {
        if (scores[i] > max)
        {
            result[0]++;
            max = scores[i];
        }
        if (scores[i] < min)
        {
            result[1]++;
            min = scores[i];
        }
    }

    return result;
}

// Complete the Birthday Chocolate function below.
int birthday(vector<int> s, int d, int m)
{
    int sum, result = 0;
    for (int i = 0; i <= s.size() - m; i++)
    {
        sum = 0;
        for (int j = 0; j < m; j++)
        {
            sum += s[i + j];
        }
        if (sum == d)
            result++;
    }
    return result;
}

// Complete the divisibleSumPairs function below.
int divisibleSumPairs(int n, int k, vector<int> ar)
{
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if ((ar[i] + ar[j]) % k == 0)
            {
                count++;
            }
        }
    }
    return count;
}

// Complete the findDigits function below.
int findDigits(int n)
{
    int digits = n;
    int cur_digit;
    int count = 0;

    do
    {
        cur_digit = digits % 10;
        digits /= 10;
        if (cur_digit != 0 && n % cur_digit == 0)
        {
            ++count;
        }
    } while (digits > 0);

    return count;
}

int main()
{
    // vector<int> v{1, 3, 2, 6, 1, 2};
    // vector<int> b{16, 32, 96};
    // cout << getTotalX(a, b);
    // cout<<birthday(v,4,1);
    // cout << divisibleSumPairs(6, 3, v);
    cout << findDigits(1012);
    return 0;
}