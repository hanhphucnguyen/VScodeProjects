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

int main()
{
    vector<int> v{0 ,0, 1, 0, 0, 1, 1, 0};
    cout<<jumpingOnClouds(v,2)<<endl;
    return 0;
}