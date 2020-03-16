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

# f = open('text.txt')
# u = f.readlines()
# count = 0
# cur = 0
# for i in range(int(u[0])):
#     count +=1
#     result = 0
#     cur += 1
#     x = int(u[cur])
#     cur += 1
#     y = int(u[cur])
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

while True:
    input_ = input()
    if not input_: 
        break
    else:
        inp = input_.replace(' ','').replace('-','')
        if len(inp) == 10:
            flag = True
            s1=[]
            s2=[] 
            result = list(inp)
            for t in range(len(result)):
                if result[t]=='X': result[t] = 10
                result[t] = int(result[t])
                if t==0: 
                    s1.append(result[t])
                    s2.append(s1[t])
                else:
                    s1.append(result[t]+s1[t-1])
                    s2.append(s1[t]+s2[t-1])
            flag = False if s2[-1]%11 !=0 else True
            print(f'{input_} is correct.') if flag else print(f'{input_} is incorrect.')
        else:
            print(f'{input_} is incorrect.')