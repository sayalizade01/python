#TUPLE()------> t1=( )
#tuple is a <class>
#tuple is immutable (unchangable)
#tuple elements are indexed
#tuple elements are sequenced
#tuple is iterable 
#tuple can contain heterogeneous elements(int,float,complex)
#to make a tuple there should be more than 1 element or

# t1=( )
# t2=(1,2,3,4)
# t3=(10)
# print(type(t1))
# print(type(t2))
# print(type(t3))  # output is int because it is single element

# t1=(1,2,3,4)
# print(t1[2]) # print element at index 2

#using for loop:
# t1=(1,2,3,4)
# for i in t1:
#     print(i,end=" ")

#using while loop:
# t2=(1,2,3,4,5)
# i=0
# while i<len(t2):
#     print(t2[i],end=" ")    
#     i+=1  

#built in methods:
# len()
# min()
# max()
# sum()
# sorted()

# t=(5,2,15,9,6,20,13)
# print(len(t))     #7
# print(min(t))     #2
# print(max(t))     #20
# print(sum(t))     #70
# print(sorted(t))  #[2, 5, 6, 9, 13, 15, 20]


#CONCATENATION AND REPEATATION OPERATOR
# t1=(1,2,9,36,40)
# t2=(5,50,500,5000)
# print(t1+t2)       #print one tuple including all elements of both tuple
# print(t1*3)        #print tuple 3 times


#COMPARISON OPERATOR:
# =- assignment , ==-comparision
# t1=(10,20,30)
# t2=(11,19,50,60.90,105)
# print(t1==t2) 
# print(t1<t2)
# print(t1>t2)

# t1=(10,20,30)
# t2=(10,20,30)
# print(t1==t2) 
# print(t1<t2)
# print(t1>t2)

#------------------------------------------------------------------------------------
#TUPLE Object methods:
# t1=(10,20,30,40,10,50,10,60,70)
# print(t1.index(30))                #2
# print(t1.count(10))                #3


#Slicing operator:
#t1=[beg    :   end       :    step]
#  included    excluded     commom grp
    
# t1=(10,20,30,40,50,60,70,80,90,100)
# print(t1[0:5:1])

# t1=(0,1,2,3,4,5,6,7,8,9,10)
# print(t1[::-1])
# print(t1[5:0:-1])
# print(t1[:10:])


#user input
t1=tuple()
print(t1)
t2=tuple([10,20,30])
print(t2)
t3=tuple(range(5))
print(t3)
t4=tuple("Sanjivani")
print(t4)