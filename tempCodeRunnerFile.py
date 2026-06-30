#Q1.traffic management

l=list(map(int,input("Enter time:").split()))
classifications={}
for i in range(len(l)):
    if l[i]<30:
        classifications[i]="fast"
    elif l[i]<=60 & l[i]>30:
        classifications[i]="Normal"

    else:
        classifications[i]="Extended"

print("Final classifications:",classifications)        

#Q2.liabrary 
# student={}
# n=int(input("Enter number of students:"))
# for i in range (n):
#     sid=input("Enter id:")
#     days=int(input("Enter  no of days:"))
#     student[sid]=days

# fines=[]
# for sid , days in student.items():
#     if days>14:
#         fine=(days-14)*10
#         fines.append((sid,fine))
# print("Students with fines:",fines)

data=["s10":20,"s20":10]
fine=[]
for sid,days in data.items():
    if days>14:
        fine=(days-14)*10
        fine.append((sid,fine))
        print(fine)

#Q3 email spam
# subject=[]
# n=int(input("Enter number of emails:"))

# for i in range(n):
#     sub=input("Enter subject:")
#     subject.append(sub)
# spam=set()
# inbox=set()
# for sub in subject:
#     s=sub.lower()
#     if "free" in s or "lottery" in s or"urgent"in s:
#         spam.add(sub)
#     else:
#         inbox.add(sub)

# print("Spam Emails:",spam)
# print("Inbox Emails:",inbox)        

#Q4.Cinema
# age=list(map(int,input("Enter list of ages of group:").split()))
# prices=[]
# base_price=200
# total=0
# for i in age:
#     if i < 12:
#         price=base_price*0.5
#     elif i>60:
#         price=base_price*0.7
#     else:
#         price=base_price
#     prices.append(price)
#     total+=price

# print("Individual prices:",prices)
# print("Total Group Bill:",total)    

#Q5 Employee Attendence
# employees=[]
# n=int(input("Number of employees?"))
# for i in range(n):
#     emp_id=input("Enter emp id:")
#     days=int(input("Enter number of days present:"))
#     employees.append((emp_id,days))

#     warning=[]
#     bonus=[]
#     for emp_id,days in employees:
#         if days<20:
#             warning.append(emp_id)
#         elif days==30:
#             bonus.append(emp_id)
# print("Warning list",warning)
# print("Bonus List:",bonus) 


#Q6.parking
# parking=[0,1,0,1,1,0,0,1,0,1,1]
# i=0
# found=False
# while i<len(parking):
#     if parking[i]==0:
#         parking[i]=1
#         print("Parking assigned at spot:",i)
#         found=True
#         break
#     i+=1
# if not found:
#     print("Parking full!")

#Q7. A restaurant manager wants to process digital customer feedback. Accept a list of 
# dictionaries, where each is formatted as {'rating': 4, 'comment': 'Good food'}. Use a loop to 
# iterate through the feedback. Calculate the average rating. Use conditional statements: 
# if a rating is 2 or below, extract the comment and append it to a specific complaints list so 
# the manager can review the negative feedback immediately.

# feedback=[]
# n=int(input("Enter how many feedbacks"))
# for i in range(n):
#  rating=int(input("Enter rating:"))
#  comments=input("Enter comments:")

# feedback={"rating:",rating,"Comment",comments}
# feedback.append(feedback)
# total=0 


#Q8. automated quiz grader
# correct={}
# n=int(input("Enter how many students:"))
# for i in range(n):
#   q=input("Enter questions:")
#   ans=input("Enter correct answer:")
#   correct[q]=ans
# student={}
# for i in range(n):
#   q=input("Enter question:")
#   ans=input("Enter students answer")
#   student[q]=ans

# score=0
# for q in correct:
#   if q in student:
#     if student[q]==correct[q]:
#       score+=2
#     else:
#       score-=1
# print("Final Score:",score)