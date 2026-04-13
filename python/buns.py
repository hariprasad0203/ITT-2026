#in this program,according to the no.of.buns available the sandwitch is made or not is displayed
bun=int(input("Enter the no of buns the shopkeeper have:"))
if bun%4==0:
   print("No sandwitch can be made")
elif bun%4==2:
   print("Yes sandwitch can be made")
else:
   print("Invalid input")
