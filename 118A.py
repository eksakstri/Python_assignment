str = input()
str1 = str.replace("a","")
str1 = str1.replace("e","")
str1 = str1.replace("i","")
str1 = str1.replace("o","")
str1 = str1.replace("u","")
str1 = str1.replace("y","")
str1 = str1.replace("A","")
str1 = str1.replace("E","")
str1 = str1.replace("I","")
str1 = str1.replace("O","")
str1 = str1.replace("U","")
str1 = str1.replace("Y","")
n = len(str1)
str1="."+str1
for i in range(2,(2*(n)),2):
    str1 = str1[:i]+"."+str1[i:] 
str1=str1.lower()
print(str1)