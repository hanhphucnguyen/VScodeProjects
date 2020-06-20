def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted 

def main():
    print(bigSorting([31415926535897932384626433832795,1,3,10,3,5]))

if __name__ == "__main__":
    main()