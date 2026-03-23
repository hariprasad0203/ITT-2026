n=input("Enter your number:")
n1=input("Enter the guess number:")
s=str(n)
s1=str(n1)
h=0
n=0
for i in range(0,len(s)):
    for j in range(0,len(s1)):
        if s[i]==s1[j] and i==j:
            h+=1
        elif s[i]==s1[j]:
            n+=1
print(h,'H',n,'N')
