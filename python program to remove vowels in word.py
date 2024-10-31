#removing vowels in word
word=input("enter any word :")
vawer="aiueoAIUEO"
my_word=[]
for x in word:
    if x not in vawer:
        my_word.append(x)
neword="".join(my_word)
print (neword)
print(my_word)
                                       
