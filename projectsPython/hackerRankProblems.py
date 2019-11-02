# Complete the workbook function below.
def workbook(n, k, arr):
    curPage = 1
    count = 0
    if n == 1 and k == 1:
        return arr[0]
    else:
        for i in arr:
            for curProb in range(1, i+1):
                if curProb > k and curProb % k == 1:
                    curPage += 1
                if curProb == curPage:
                    count += 1
            curPage += 1

        return count


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):

    if len(c) == n:
        return 0
    else:
        result = 0
        min = 0
        c.sort()
        l = abs(c[0]-0)
        r = abs(c[len(c)-1] - (n-1))
        for i in range(len(c)-1):
            left = c[i]
            right = c[i+1]
            temp = (right-left)//2
            if min < temp:
                min = temp
        result = max(min, l, r)
        return result


# Complete the fairRations function below.
def fairRations(B):
    count=0
    if sum(B) % 2 != 0:
        return "NO"
    else:
        for i in range(len(B)-1):
            if B[i]%2 !=0: 
                B[i] +=1
                B[i+1] += 1
                count +=2
        if sum(B)%2 != 0:
            return "NO"
        else:
            return count

# Complete the introTutorial function below.
def introTutorial(V, arr):
    for i in arr:
        if i==V:
            return arr.index(i)


def main():

    # p= open('input.txt','rt')
    # a = p.read().split()
    # for i in range(0, len(a)): 
    #     a[i] = int(a[i]) 

    # print(workbook(5,3,[4,2,6,1,10]))
    # print(flatlandSpaceStations(100, [93, 41, 91, 61, 30, 6, 25, 90, 97]))   
    # print(fairRations(a))
    print(introTutorial(4,[1,2,3,4]))


if __name__ == "__main__":
    main()
