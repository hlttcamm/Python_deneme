# 1
agg=0
for x in range(101):
    agg+=x
print(agg) 

# 2
for x in "abc": #for string variable, x take value which is each character of "abc" string
    print(x)

# 3
    for x in range(5):
    print(x)

# 4
 x='hey''
index=0
while index<=len(x):
    print(x[index])
    index+=1

# 5   
 for i in range(10):
    if i==4:
        break
    print(i)   

# 6
i=0
while (i<10):
    if(i==3 or i==5):
        continue
    print("i:", i)
    i+=1

# 7
l=[1,2,3]
len(l)
l.append(42)
l

# 8
l=[1,2,3,4] #copy() ile Aliasing (Adres Paylaşımı önlenir)
l1=l.copy()
l[0]='irem'
print(l)
print(l1)

#agg=0
notlar=[60,40,50]
for i in notlar:
  agg+=i
print("avarage of students' score: ",agg/len(notlar) )