"""a=input('Enter 1st  no :')
b=input('Enter 2nd no :')
c=int(a)+int(b)
print(c)"""


"""l=input('Enter a Length :')
w=input('Enter a Width :')
a=int(l)*int(w)
print(a)"""


"""r=input('Enter a Radius :')
pi=3.14
a=float(pi)*int(r)*int(r)
print(a)"""

"""b=input('Enter a side :')
a=int(b)*int(b)
print(a)"""

"""b=input('Enter a base :')
h=input('Enter a height :')

a=0.5*int(b)*int(h)
print(a)"""

"""print('hello' ,end=' ')
print('Aasha')"""

"""p= input('Enter a principal :')
r= input('Enter a rate :')
t= input('Enter a time :')
si=int(p)*int(r)*int(t)/100
print(si)"""


'''C= input('Enter a centigrade :')
F= input('Enter a fahranheit :')
F = (float(C) * 9/5) + 32
C = (float(F) - 32) * 5/9

print(F)
print(C)'''


'''a= input('Enter 1st Name :')
b= input('Enter 2nd Name :')
c=a
a=b
b=c
print(a)
print(b)'''

'''a,c,b=10,20,30
print(a)
print(b)
print(c)
x,y="sanju",500
print(x,y)
m=n=10
print(m,n)'''

'''st1 = "Sanju"
st2 = """
Aasha
Kiran
Sanju
"""
st3 = '''
'''Aasha
Kiran
Sanju'''
'''
print (st1)
print (st2)
print (st3)
for x in st1:
    print(x,end=" ")'''
"""    
''' string ko check kern ka method. '''
st1 = "I am good gril."
print("I" in st1)
print("I" not in st1)
''' string ko cut kern ka method. '''
st2 = "I am good gril."
print(st2[1:4])
print(st2[-0:-5])
''' string ko lower and upper kern ka method. '''
st3 = "I am good gril."
print(st3.lower())
print(st3.upper())

''' string me sapce dena ka kam kerta hai. '''
st4 = "   I am good gril.   "
print(st4.strip())

''' string ko replace kern ka method. '''
st5 = "   I am good gril.   "
print(st4.replace("good","cute"))

''' Creates  list of strings.'''
st6 = "   I am good gril.   "
print(st6.split())
"""
#formating String
'''Complete=18
currnt=19
print ('Asha has Completed '+str(Complete)+' years.')
#text='Asha has Completed '{}' years.'
#print(text.format(Complete))
text='Asha has Completed 18 years.'
print (text.capitalize())
print (text.upper())
print (text.lower())
print ('TEXT'.isupper())
print (text.title())
print (text.swapcase())
print (text.count('e'))
print (text.lower().count('a'))
print (text.endswith('rs.'))
print (text.startswith('As'))
name="SanjuRawat "
number=" 123"
space="  hi"
print (name.index('n'))
print (name.index('a'))
print (name.rindex('a'))
print (name.isalpha())
print (number.isalpha())
print (name.isnumeric())
print (number.isnumeric())
print (space.isspace())
print (number.isspace())
a=name+number.strip()+space
x=name.rstrip()+number.strip()+space.strip()
print(x)
print(a)
s="""hi
sanju
rawat
"""
b=s.splitlines()
s1="hi"
print(b)
print(s1.zfill(3))
print(bool(10-12))
print(bool(10-10))
print(bool(10-9))'''
# Escape sequences
'''
print ('Hello \n World')
print ('Hello \b World')
print ('Hello \t World')
print ('Hello \' World')
print ('Hello \b\b World')
print ("Hello\" World")
print ('Hello World\U0001F604')
# range() function
# range([start],end,[ind/dec])
a=range(5)
print (a[0],a[1],a[2],a[3],a[4])
a=range(0,5,2)
print (a[0],a[1])
a=range(2,5)
print (a[0],a[1],a[2])
# Contorl Statments - If
a=20
b=10
if a>b :
    print("a is greater")
print("No Masti")
# If - else
a=20
b=10
if a<b :
    print("a is greater")
else :
    print("b is greater")
print("No Masti")'''
# elif
'''a=input("Enter a percentage :")
b = float(a)
if b>=36 :
    print("Pass")
else :
    print("Fail")'''

'''a=input("Enter a no :")
b = int(a)
if b>0 :
    print("Positive")
elif b<0 :
    print("Negative")
else :
    print("Zero")'''
'''a=input("Enter One no :")
b=input("Enter Two no :")
c=input("Enter Three no :")

if int(a)>int(b) :
    print(a)
elif int(b)>int(c) :
    print(b)
else :
    print(c)



for i in range (1,50,1) :
    if i%2==0 :
      print (i)
text="Sanju"
for i in text :
    print(i)
    
#Accessing List Elements
a=[1,2.2,'anli',3]
for x in a :
    print(x)
#list in while    
i=0
x=len(a)
while i<x :
    print(a[i])
    i+=1
    
i=0
x=len(a)
while i<x :
    print(a[i])
    if (i==3) : break
    i+=1
    
for i in range(4) :
    for i in range(3) :
      print(i,end=" ")
    print()

n = int(input("Enter a no."))
p=0
for i in range(2,n):
    if n%i == 0:
        p=1
        
if p==1:
        print("Not Prime")
else:
        print("Prime")



n = input("Enter a no.")
p=0
for i in n:
    if i=='a' or i=='A'or i=='e'or i=='E'or i=='i'or i=='I'or i=='o'or i=='O'or i=='u'or i=='U':
        p=p+1

print(p)

a=input('Enter a name :')
str=""
for i in a:
    str=i+str
print(str)'''

'''a=5
for i in range(0,a,1) :
    for j in range(0,a,1) :
     print('*')
print(end=" ")
'''
'''num1=int(input('Enter a no:'))
num2=int(input('Enter a no:'))
c=num1**num2
print(c)
a=int(input('Enter a no:'))
num1=a-1
num=0
rev=0
while a-1>0:
   num=int(a)%10
   rev=(rev*10)+int(num) 
   a=int(a)/10
print(rev)'''
'''a=5
for i in range(a,1,-1) :
       for j in range(i-1) : 
           print('*',end=" ")
           j= j+1
         
       print()'''

#patten
'''for i in range(6) :
       for j in range(i) : 
           print('*',end=" ")
       print()
#output
*
* *
* * *
* * * *
* * * * *'''
#patten
for i in range(6,1,-1) :
       for j in range(1,i) : 
           print(j,end=" ")

       print()
'''output
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 '''
#patten
for i in range(5,0,-1) :
       for j in range(i) : 
           print(i,end=" ")

       print()
'''output
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
#patten
for i in range(5,0,-1) :
       for j in range(i) : 
           print("*",end=" ")

       print()
'''output
* * * * *
* * * *
* * *
* *
*
'''
#patten
i=8
for i in range(8,1,-2) :
       for j in range(1,i+1) : 
           if i<=j :
             print(" *",end=" ")
           else:
             print(" ")
       print()
'''output

'''
'''#Nested Loop
list1 = ["tamatar","kanda"]
list2=[" is good.","is not good"]
for i in list1 :
       for j in list2 : 
           print(i+j)

#list
list1=[10,20,30,40,50,60]
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

print(list1[3:4])
print(list1[3:])
print(list1[:3])
print(list1[-4:-1])'''
'''
What is a vehicle ?
Answar:-A vehicle is a machine such as a car, bus, or truck which has an engine and is used to carry people from place to place.
How do we use vehicles?
Answer:-Vehicles can be operating on road, water or air. The needs can be mostly carrying cargo, transporting people, adventure sports, and also emergencies. There are different vehicles for travel, cargo and also hybrid vehicles that carry both.

'''
#list items are ordered ,changeable(mutable) and allow duplicate values.
#(::)
list1 = [1,2,3,4,5,6]
print (list1[:2:1])
print (list1[::])
print (list1[::1])
print (list1[::-1])
print (list1[::2])
print (list1[:1:1])

list2 = [1,2,3,4,5,6]

for list2 in range(6,0,-1) :
    print(list2,end=" ")
print()   
i=6   
while i>=list2:
    print(i,end=" ")
    i=i-1
    
#changeable
'''list2[1] = 12
print(list2)

#duplicate
list2.append('asd')
print(list2)'''
list1=['a','b','c','d','e']
print(list1)
list1[1:3]=['y','x']
print(list1)
list1[1:3]=['x']
print(list1)
list1[1:3]=['x','y','m','n']
print(list1)
list1.insert(2,'sanju')
print(list1)
list1.remove('m')
print(list1)
list2=['t','q','z']
list1.extend(list2)
print(list1)
list3=list2
print(list2)
print(list3)
list2[2]='sdfg'
print(list2)
print(list3)

list4=['anil','sunil','sonu','sanju','asha']
print(list4.pop())
print(list4)
print(list4.pop(2))
print(list4)
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
list5=['anil','sunil','Sonu','sanju','asha']
list5.sort()
print(list5)
list5.sort(key=str.lower)
print(list5)
list5.reverse()
print(list5)
#same memory loction
list6=list5
list5[2]='ram'
print(list5)
print(list6)
#differn memory loction
list6=list5.copy()
list6[4]='t'
print(list6)
print(list5)

list1=[1,2,3]
list2=[4,5,6]

for i in list2:
    list1.append(i)
    
print(list1)
list1 = [1,2,3,4,5,6,7]
list2 =[]
for i in list1 :
    list2.append(i)
print(list2)

# list comprehestion
list2=[i for i in list1 if i%2==0]
print (list2)

list3=[i for i in range(5,10)]
print (list3)

list2=["Sanju" for i in list1]
print (list2)
#---------------------
#List Reversal
list1=[1,2,4,5,6,7]
print (list1[::-1])
#List Concatenation
list2=[1,2,3]
list3=[4,5,6]
for i in list3 :
    list2.append(i)
print(list2)
#List Frequency Count
n=int(input("Enter a no:"))
c=0
list4=[1,3,2,1,5,3,2,3,8]
for i in list4:
    if i==n:
        c=int(c)+1;
print(c)
#List Filtering
a=int(input("Enter a no:"))
list5=[1,2,3,4,6,7,8,9,5]
for i in list5 :
    if i<n :
        print(i)
#List Palindrome Check
list1=[1,1,2,1,1]

if list1==list1[::-1] :
    print("Palindrome")
else:
    print("Not Palindrome")
#List Sorting (Bubble sort)
list1=[1,1,2,1,1]
tmp=0
for i in range(0,len(list1)) :
    for j in range(0,len(list1)):
        if list1[i]<list1[j] :
            tmp=list1[i]
            list1[i]=list1[j]
            list1[j]=tmp
 
print(list1)

#List Intersection
list1=[1,1,2,4,3]
list2=[2,1,3,5,6]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
            
            
print(list3)