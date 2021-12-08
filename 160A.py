n = int(input())
arr = []
sum1 = 0
sum2 = 0
arr = list(map(int, input().split()))
if n!=1:
    for j in range (0,(n-1)):
        for k in range(0,(n-1)):
            if arr[k]<arr[k+1]:
                a = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = a 
    for l in range(0,n):
        sum1 = 0
        sum2 = 0
        for x in range(0,l):
            sum1 = sum1+arr[x]
        for y in range(l,n):
            sum2 = sum2+arr[y]
        if sum1>sum2:
            break
        if sum1==sum2:
            l=l+1
else:
    l=1
print(l)
