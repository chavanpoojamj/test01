#n!=n*(n-1)!

def factorial(n):
    if n==0 or n==1:
     return 1
    return n * factorial(n-1)


f=factorial(7)
print(f)
