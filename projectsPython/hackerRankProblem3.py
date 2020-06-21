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
    
def main():
    # print(bigSorting([31415926535897932384626433832795,1,3,10,3,5]))
    print(alternatingCharacters('AAAA')) 

if __name__ == "__main__":
    main()