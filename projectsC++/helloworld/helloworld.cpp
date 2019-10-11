#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Complete the dayOfProgrammer function below.
string dayOfProgrammer(int year)
{
    string result = "";
    if (year < 1918)
    {
        if (year % 4 == 0)
            result = "12.09." + to_string(year);
        else
        {
            result = "13.09." + to_string(year);
        }
    }
    else
    {
        if (year > 1918)
        {
            if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
                result = "12.09." + to_string(year);
            else
            {
                result = "13.09." + to_string(year);
            }
        }
        else
        {
            result = "26.09." + to_string(year);
        }
    }
    return result;
}

int pageCount(int n, int p)
{
    int count, cur;
    count = 0;

    if ((n / 2) >= p)
    {
        cur = -1;
        do
        {
            cur += 2;
            cur == 1 ? count = 0 : count++;
        } while (cur < p);
    }
    else
    {
        n % 2 == 0 ? cur = n + 2 : cur = n + 1;
        do
        {
            cur -= 2;
            if ((cur == n) || (cur == n - 1))
            {
                count = 0;
            }
            else
            {
                count++;
            }

        } while (cur > p);
    }
    return count;
}

int countingValleys(int n, string s)
{
    int count = 0;
    int valley = 0;
    bool flag;
    for (int i = 0; i < n; i++)
    {
        count == 0 ? flag = true : false;
        if (s[i] == 'U')
            count++;
        else
            count--;
        if (count < 0 && flag)
        {
            valley++;
            flag = false;
        }
    }
    return valley;
}

/*
 * Complete the getMoneySpent function below.
 */
int getMoneySpent(vector<int> keyboards, vector<int> drives, int b)
{

    int mink, mind, result;
    mink = keyboards[0];
    for (int i = 0; i < keyboards.size(); i++)
    {
        if (keyboards[i] < mink)
            mink = keyboards[i];
    }
    mind = drives[0];
    for (int i = 0; i < drives.size(); i++)
    {
        if (drives[i] < mink)
            mind = drives[i];
    }
    if (mink + mind > b)
        return -1;
    else
    {
        result = mind + mink;
        for (int i = 0; i < keyboards.size(); i++)
        {
            for (int j = 0; j < drives.size(); j++)
            {
                if ((keyboards[i] + drives[j] > result) && (keyboards[i] + drives[j] <= b))
                    result = keyboards[i] + drives[j];
            }
        }
        return result;
    }
}

string catAndMouse(int x, int y, int z)
{
    int range1, range2;
    x - z > 0 ? range1 = x - z : range1 = z - x;
    y - z > 0 ? range2 = y - z : range2 = z - y;

    if (range1 == range2)
        return "Mouse C";
    else
    {
        if (range1 > range2)
            return "Cat B";
        else
            return "Cat A";
    }
}

/*
 * Complete the 'pickingNumbers' function below.
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

int pickingNumbers(vector<int> a)
{
    int count, cur, max;
    max=0;
    for (int j = 0; j < a.size(); j++)
    {
        cur = a[j];
        count = 0;
        for (int i = 0; i < a.size(); i++)
        {
            if ((cur - a[i] >= 0) &&(cur - a[i]<=1)) 
                count++;
        }
        if (max < count) max=count; 
        count=0;
       
        for (int i = 0; i < a.size(); i++)
        {
            if ((cur - a[i] <= 0) &&(cur - a[i]>=-1)) 
                count++;
        }
        if (max < count) max=count;
    }
    return max;
}

int main()
{
     vector<int> v{4,6,5,3,3,1};
    // cout<<dayOfProgrammer(2016);
    cout << pickingNumbers(v);
    return 0;
}