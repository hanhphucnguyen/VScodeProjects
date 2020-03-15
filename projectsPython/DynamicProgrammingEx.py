# cache = {}
# def fibo(n):
#     if n in cache:
#         return cache[n]
#     else:
#         if (n<2): return n 
#         else:
#             cache[n] = fibo(n-1)+ fibo(n-2)
#             return cache[n]
# print(fibo(60))

cache = [0,1]
def fiboBottomup(n):
    for i in range(2,n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache.pop()
    
print(fiboBottomup(60))
