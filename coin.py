a=int(input("Enter the number of coins for suresh:"))
b=int(input("Enter the number of coins for sudar:"))
c=int(input("the coins raja gave to loser:"))
d=int(input("the coins given by sures:"))
if a < b:
   a+=c
   e=a
   print("S")
else :
   b+=c
   f=b
   print("N")
if e > b:
   b+=d
   print("N")
else:
   a+=d
   print("S")
