#---------------------------------------------
# external case

# inputV = int(input())
# for i in range(inputV):
#     x = int(input())
#     y = int(input())
#     print(f'Case {count}: {result}')


# inputV = int(input())
# count = 0
# for i in range(inputV):
#     count +=1
#     result = 0
#     x = int(input())
#     y = int(input())
#     for j in range(x,y+1):
#         if j%2 !=0 : result +=j
#     print(f'Case {count}: {result}')

#-------------------------------------------------
# until no case input

# while True:
#     i = input()
#     if not i: 
#         break
#     else:
#         i = i.replace(' ','').replace('-','')
#         print(f'result:{i}')

# while True:
#     try:
#         input_ = input()
#         if input_ == '':
#             break
#         inp = input_.replace(' ','').replace('-','')
#         out = input_.strip()
#         if len(inp) == 10:
#             flag = True
#             s1=[]
#             s2=[] 
#             result = list(inp)
#             for t in range(len(result)):
#                 if result[t] == 'X':
#                     if t==len(result)-1: 
#                         result[t] = 10
#                     else:
#                         flag = False
#                         break
#                 elif result[t] == 'x':
#                     flag = False
#                     break
#                 result[t] = int(result[t])
#                 if t==0: 
#                     s1.append(result[t])
#                     s2.append(s1[t])
#                 else:
#                     s1.append(result[t]+s1[t-1])
#                     s2.append(s1[t]+s2[t-1])
#             if len(s2)==len(result) and s2[-1]%11 ==0: 
#                 flag = True
#             else:
#                 flag = False
#             print(f'{out} is correct.') if flag else print(f'{out} is incorrect.')
#         else:
#             print(f'{out} is incorrect.')
#     except EOFError:
#         break

while True:
    inp = input()
    if not inp:
        break
    else:
        result = 0
        arr = list(inp)
        arrSorted = sorted(arr)
        if arr == arrSorted: 
            for i in arr:
                print(ord(i)-96)











#-------------------------------------------------
# until right stop case input

# while True:
#     iput = input()
#     ar = [int(i) for i in iput.split()]
#     if ar[0] == 0 and ar[1]==0: 
#         break
#     else:
#         pass

# while True:
#     iput = input()
#     ar = [i for i in iput.split()]
#     if ar[0] == '0' and ar[1]== '0': 
#         break
#     else:
#         leftNum = [int(i) for i in list(ar[0])]
#         rightNum = [int(j) for j in list(ar[1])]
#         leftNum = [i for i in reversed(leftNum)]
#         rightNum = [i for i in reversed(rightNum)]
#         count = min(len(leftNum),len(rightNum))
#         cp = 0
#         hold = 0
#         for i in range(count):
#             if leftNum[i] + rightNum[i] + hold > 9: 
#                 cp += 1
#                 hold = 1
#             else:
#                 hold = 0
#         if cp == 0:
#             print('No carry operation.')
#         elif cp == 1:
#             print('1 carry operation.')
#         else:
#             print(f'{cp} carry operations.')

# while True:
#     a, b = map(int , input().split())
#     cnt = 0
#     if(a == 0 and b == 0):
#       break
#     c = 0
#     for i in reversed(range(10)):
#       c = a%10 + b%10 + c
#       if c > 9:
#         c = 1
#       else:
#         c = 0
#       cnt += c
#       a //= 10
#       b //= 10
      
#     if cnt == 0:
#       print('No carry operation.')
#     elif cnt == 1:
#       print('%d carry operation.' %cnt)
#     else:
#       print('%d carry operations.' %cnt)