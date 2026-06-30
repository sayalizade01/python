#LIST:
#1 list is a <class>
#2 list is a iterable sequence
#3 list is mutable(changable).{array is immutable(non - chnagable)}
#5 List is growable
#5 List can contain heterogeneous data . eg:[ 20  ,  35.5  ,  True  ,  "Sanjivani "]
#                                             int     float    bool       string
#6 List are indexe


#CHECK TYPE:
#homogeneous-
# a1=[20,10,30,40,50]
# print(type(a1))
# print(a1)  #a1 is a list 
# 

#heterogenous:
# l1=["Sayali",20,50.55,True]
# print(type(l1))

#Blank:
# l2=[]
# print(type(l2))

#concept of  negative indexing:
#   -5  -4  -3  -2  -1
#l=[10, 20, 30, 40, 50]
#   0   1  2  3  4
 
# l2=[10,20,15,35,60,90]
# l1=[-1]
# print(l1) #here 

#how to delete element in list 
# l1=[20,30,50,80,110,90]
# del l1[3]
# print(l1)

#how to edit the list
# l1=[10,20,30,40,50]
# l1 [3]=83
# print(l1)

#----by -ve index
# l1=[20,30,50,80,110,90]
# l1[-1]=100
# print(l1)

#print list with loop 
#1 for loop:
# l1=[10,20,30,40,50]
# for i in l1:
#     print(i,end=" ")

#2 while loop:
# l1=[10,20,30,40,50]
# i=0                   #index 0
# while i<5:            # 5 can be replaced by len(l1)
#     print(l1[i],end=" ")
#     i+=1

#-------------------------------------------------------------------------------
#PACKING AND UNPACKING:
# l1=[1,2,3,4,5,6]
# a,b,c,d,e,f=l1       #unpacking     
# print(c)

# a=10,b=20,c=30
# l=[a,b,c]
# print(l)    # packing

#------------------------------------------------------------------------------------------
#BUILT IN METHODS:
#len-->  no. of elements,length
#sum--->sum of all no.
#max---> find maximum
#min--->find minumum
#sorted---> arrange krun deta

# l=[10,30,20,60,40,50]
# print(len(l))
# print(sum(l))
# print(max(l))
# print(min(l))
# print(sorted(l))
# print(l)

#------------------------------------------------------------------------------------------------
#LIST METHOD:
# l=list(range(4))
# print(l)          #// [0,1,2,3]

# l=list("Sanjivani")
# print(l)             #// s a n j i v a n i ---- iterable sequence

#-------------------------------------------------------------------------------------------------
#COMPARISION OPERATOR:
# l1=[1,2,3,]
# l2=[2,3,1]
# l3=[1,2,3,4,5]
# l4=[2,3,1]
# print(l1==l2)
# print(l1>l2)
# print(l2==l4)

#CONCATALATION OPERATOR:
# l1=[1,2,3,4,6]
# l2=[5,7,8,9,10]
# l3=l1+l2
# print(l3)

#REPEATATION OPERATOR:
# l1=[2,4]
# l2=l1*2
# print(l2)

#LIST OF LISTS:
# l1=[[1,2,3],[4,5],9]
# print(l1[0][2])    #// to find the 3 of first list.

#LIST OBJECTS:
#1.append()-we cant direct call this func, so we write l.append (used to add a element in list)-append(value)
# l1=[1,2,3,4,7]
# l1.append(10)
# print(l1)

#2.insert()-to add it in between,middle of list ,insert(index,value)
# l1=[1,2,3,4,5]
# l1.insert(2,10)
# print(l1)  
#            #// 10 added at index 2
#3.remove()-to remove an element from list-remove(value)
# l1=[1,2,3,4,5]
# l1.remove(3)
# print(l1)

#4.pop()-remove or delete element,also return that element-pop(),pop(index)-delete method
# l1=[1,2,3,4,5]
# l1.pop()
# print(l1)

# l1=[1,2,3,4,5]
# l3=l1.pop(1)
# print(l3)

#5.Clear()- 
# l1=[10,20,30]
# print(l1.clear(),l1)

#6.reverse()-reverse list
# l=[10,20,30]
# print(l.reverse(),l)

#7.Sort()-list ko arrange list
# l=[10,20,3,2,50,7]
# print(l.sort(),l)
# print(l)

# l=[10,20,3,2,50,7]
# print(sorted(l),l)
# print(l)

#8.index()-to find out the index of the element in list -index()
# l=[10,20,30,40,50,60]
# print(l.index(60))

#9.count()-count in list
# l=[10,10,10,20,30,10,10,10]
# print(l.count(10))

#LIST COMPREHENTION:
# a=1
# print([a**2 for i in range(4)])

# print([i for i in range(0,20,2)])

# print(([i for i in range (20)if i%2==0]))