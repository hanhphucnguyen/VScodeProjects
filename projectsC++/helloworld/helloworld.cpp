#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>

using namespace std;

// Complete the cavityMap function below.
vector<string> cavityMap(vector<string> grid)
{
    vector<string> result;
    string temp;
    for (int i = 0; i < grid.size(); i++)
    {
        temp="";
        for (int j = 0; j < grid[i].size(); j++)
        {
            if (i - 1 >= 0 && i + 1 < grid.size() && j - 1 >= 0 && j + 1 < grid[i].size() && grid[i - 1][j] < grid[i][j] && grid[i + 1][j] < grid[i][j] && grid[i][j - 1] < grid[i][j] && grid[i][j + 1] < grid[i][j])
                temp += 'X';
            else
            {
                temp += grid[i][j];
            }
        }
        result.push_back(temp);
    }
    return result;
}

int main()
{
    // vector<string> v{"1112", "1912", "1892","1234"};
    // vector<string> test = cavityMap(v);

    return 0;
}