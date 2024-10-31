#lowercamelcase to snake case
word=input("enter lowercamel case: ")
word1=[]
befor=[]
after=[]
for letter in word:
    word1.append(letter)
    
for x in range (len(word)):
    if word1[x].isupper():
        index=x
        break
for y in range(index):
    befor.append(word1[y])
for z in range(index,len(word)):
    after.append(word1[z])
first="".join(befor)
second="".join(after)
snakecasa="_".join([first,second.lower()])    
print("snake case :")
print(snakecasa)
