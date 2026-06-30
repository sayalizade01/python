#STRING
#-str is a class
#-str is immutable(not changable)
#-str is hasable()unique no. for each object.
#-str is iterable(work from 1st to last)
#-str is a sequence
#no append,no insert
#---------------------------------------------------------------------------------------- 
#A=" "    (empty)
#A="""  """ (empty)
#A=''' ''' (empty)
#A=str( )   (empty)

# a=""5""
# print(a)


#---------------------------------------------------------------------------------------

# A=str(2)
# print()
# print(type(A)) 

#--------------------------------------------------------------------------------------
#indexing.
# M="Sanjivani"
# print(M)
# print(M[5])  
# 

#loop
# s = "sanjivani"
# print(s[4])
# for i in s:
#     print(i, end="- ")
#-------------------------------------------------------------------------------

#built in methods:
#len()
# min()
# max()
# sum()
# sorted()

# s="DBAEFC"
# print(len(s))
# print(max(s))
# print(min(s))
# print(sorted(s))

# s="DBAEFC"
# sum(s)
# print(s)


#---------------------------------------------------------------------------------
#split:
# s="sanjivani educational group"
# s1=s.split(" ")
# print(s1)

#join:
#syntax: strobject.join()
# s="sanjivani educational group"
# s1=s.split(" ")
# print(s1)
# s2=' # '.join(s1)
# print(s2)

#------------------------------------------------------------------------------------------------
#slicing operator:
#syntax: str object[beg:end:stepvalue]
# s1="Sanjivani educational group"
# print(s1[0 : 20:-1])  # print till sanjivani educationa

# s1="Sanjivani educational group"
# print(s1[: :-1])  #print the string reverse
