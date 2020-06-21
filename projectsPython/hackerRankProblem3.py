def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted 

def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count += 1
    return count
    
def main():
    # print(bigSorting([31415926535897932384626433832795,1,3,10,3,5]))
    print(alternatingCharacters('AAAA')) 

if __name__ == "__main__":
    main()