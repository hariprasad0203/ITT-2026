a=int(input("Enter the number of tyres:"))
if a%4==0:
   print("No vehicle can be made")
elif a%4==2:
   print("Only the bike can be manufactured")
else:
   print("invalid input")
