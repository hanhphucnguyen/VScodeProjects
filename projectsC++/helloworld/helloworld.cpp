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
    int valley =0;
    bool flag;
    for (int i = 0; i < n; i++)
    {
        count==0 ? flag=true:false;
        if (s[i] == 'U')
            count++;
        else
            count--;
        if(count<0 && flag) {
            valley++; 
            flag=false;
        }
    }
    return valley;
}

int main()
{
    // vector<int> v{1, 4, 4, 4, 5,3};
    // cout<<dayOfProgrammer(2016);
    cout << pageCount(2, 1);
    return 0;
}