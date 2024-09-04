#to print even no.using for loop 
for i in range(0,22,2):
    print (i)

i=0
while i<=20:
    print(i)
    i=i+2


list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for a in list1:
    if a%2==1:
        list2.append(a)
print(list2)
list1[0]

for a in range(0,len(list1)):
    if list1[a]%2==0:
     list2.append(list1[a])
print(list2)


list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
a=0
while a<len(list1):
    if list1[a]%2==0:
        list2.append(list1[a])
    a=a+1
print(list2)
