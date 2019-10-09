#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Complete the dayOfProgrammer function below.
string dayOfProgrammer(int year) {
    string result="";
    if (year<1918)
    {
        if (year %4 ==0) 
            result = "12.09." + to_string(year);
            else
            {
               result = "13.09." + to_string(year);
            }           
    }else 
    {
       if (year>1918)
       {
            if ((year %400 ==0) || (year%4==0 && year%100 != 0))
            result = "12.09." + to_string(year);
            else
            {
               result = "13.09." + to_string(year);
            }  
       }else
       {
           result = "26.09." + to_string(year);
       }      
    }
    return result;
}

int main()
{
    // vector<int> v{1, 4, 4, 4, 5,3};
    cout<<dayOfProgrammer(2016);
    return 0;
}