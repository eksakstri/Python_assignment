arr = [list(map(int, input().split())) for m in range (0,5)]
i=0
j=0
f=0
for x in range(0,5):
    for y in range(0,5):
        if arr[x][y]!=0:
            i=x
            j=y
            f=1
            break
    if f==1:
        break 
if i>2:
    a=i-2
    if j>2:
        b=j-2
    else:
        b=2-j
else:
    a=2-i
    if j>2:
        b=j-2
    else:
        b=2-j
print(a+b)