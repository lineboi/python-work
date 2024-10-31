coins=[25,10,5]
total=0
for x in range(1,50):
   num=int(input("choose coin between  25 10 5 "))
   if num not in coins:
      print("wrong input")
      continue

   total+=num
   remain=50-total
   if  remain==0:
      print ("well dane")
      break
   
   if remain > 0:
        print(f"Amount due: {remain} cents")
   else:
        print(f"Excess payment. Change owed: {-remain} cents")
