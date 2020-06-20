def bigSorting(unsorted):
    for i in sorted([int(s) for s in unsorted]):
        print(i)

def main():
    bigSorting([31415926535897932384626433832795,1,3,10,3,5])

if __name__ == "__main__":
    main()