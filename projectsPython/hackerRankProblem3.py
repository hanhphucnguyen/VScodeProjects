def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted 

def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count += 1
    return count

def theLoveLetterMystery(s):
    return sum(abs(ord(s[i])-ord(s[-1-i])) for i in range(len(s)//2))

def funnyString(s):
    ns=[abs(ord(s[i])-ord(s[i+1])) for i in range(0,len(s)-1,1)]
    rns=[abs(ord(s[i])-ord(s[i-1])) for i in range(len(s)-1,0,-1)]
    return 'Funny' if ns ==rns else 'Not Funny'

def twoStrings(s1, s2):
    return "YES" if set(s1).intersection(set(s2)) else "NO"

from collections import Counter
def gameOfThrones(s):
    # Complete this function
    num_odd = 0
    s1 = Counter(s)
    for each in s1.values():
        if each % 2 != 0:
            num_odd += 1
            # when num_odd > 1, not palindrome
            if num_odd > 1:
                return 'NO'
    return ('YES')

def closestNumbers(arr):
    arr.sort()
    min_dif = abs(arr[0]-arr[1])
    ans = []
    for i in range(len(arr)-1):
        d = abs(arr[i]-arr[i+1])
        if d==min_dif:
            ans += [arr[i], arr[i+1]]
            min_dif =d
        elif d<min_dif:
            ans = [arr[i], arr[i+1]]
            min_dif =d
    return ans

def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse=True)
    a = 0
    for i in range(len(calorie)):
        a += calorie[i]*pow(2, i)
    return a
    
def main():
    # print(bigSorting([31415926535897932384626433832795,1,3,10,3,5]))
    print(alternatingCharacters('AAAA')) 

if __name__ == "__main__":
    main()