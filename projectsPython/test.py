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

# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for num, name in enumerate(presidents, start=1):
#     print("President {}: {}".format(num, name))

# for num, name in enumerate(presidents):
#     print("President {}: {}".format(num, name))

# for num in enumerate(presidents):
#     print(num)

# a = 'abcde'
# def reString(s):
#     if len(s)<=1:
#         return s
#     else:
#         i = s[len(s)-1]
#         s = s[:len(s)-1]
#         return i + reString(s)
# print(reString(a))

# print('abc', end = ' ')
# print('def')