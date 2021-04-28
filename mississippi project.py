word=input("enter a string ")
print("string is ", word)
import operator
d= {}
for x in word:
    if x in d.keys():
         d[x]+=1
    else:
         d[x]=1

asc = dict(sorted(d.items(), key=operator.itemgetter(1)))

dsc = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(dsc)
