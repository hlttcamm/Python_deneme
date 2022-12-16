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

# 9
#agg=0
notlar=[60,40,50]
for i in notlar:
  agg+=i
print("avarage of students' score: ",agg/len(notlar) )

# 10

scores=[90,72,81,77]
for i in range(len(scores)):
    if i==1:
     continue
     scores[i]+=5
print("rearanged scores: ", scores)    

# 11
#Finding determined numbers in List
x=int(input("Which number are you looking for?"))
l=[2,3,40,100,10,1]
for i in range(len(l)):
    if x==l[i]:
        print("number being looked is available")
        break
 # 12
 list={'ali':90,'veli':80,'can':45}
for i in list:       # i sırasıyla listenin value değerlerini alacak!!!
    score=list[i]
    if score>=70:
        print("Person passing lesson: ",i)
  # 13
  list={'ali':90,'veli':80,'can':45}
for i in list:       # i sırasıyla listenin value değerlerini alacak!!!
    score=list[i]
    if score>=70:
        print("Person passing lesson: ",i)
