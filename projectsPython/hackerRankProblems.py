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
# def flatlandSpaceStations(n, c):
#     result=0
#     for i in range(n):
#         min = 0
#         temp=0
#         if i not in c:
#             for j in c:
#                 if j == c[0]:
#                     min = abs(i-j)
#                 else:
#                     temp = abs(i-j)
#                     if  min>temp:
#                         min=temp
#         if result < min:
#             result=min

#     return  result


def flatlandSpaceStations(n, c):
   
    if len(c) == n:
        return 0 
    else:
        result = 0
        min = 0
        c.sort()
        l = abs(c[0]-0)
        r = abs(c[len(c)-1]- (n-1))
        for i in range(len(c)-1):
            left = c[i]
            right = c[i+1]
            if (right-left)%2 == 0:
                temp = (right - left) // 2
            else:
                temp = (right - left) // 2 + 1
            if min<temp: min=temp
        result = max(min,l,r)
        return result


def main():
    # print(workbook(5,3,[4,2,6,1,10]))
    print(flatlandSpaceStations(20, [13, 1, 11, 10, 6]))


if __name__ == "__main__":
    main()
