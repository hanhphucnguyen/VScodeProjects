

# Complete the workbook function below.
def workbook(n, k, arr):
    curPage=1
    count=0
    if n==1 and k==1:
        return arr[0] 
    else:       
        for i in arr:
            for curProb in range(1,i+1):
                if curProb > k and curProb % k==1:
                    curPage +=1
                if curProb==curPage: 
                    count +=1
            curPage +=1
        
        return count
    

def main():
    print(workbook(5,3,[4,2,6,1,10]))

i = [1,2,3,4,5]
j = (1,2,3,4)
k = {1:'ff',2:'gg'}
for a,b in k.items:
    print(f'{a}{b}')
if __name__ == "__main__":
    main()