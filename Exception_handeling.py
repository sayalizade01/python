#>the program stops normal exception
#>python generates a error message
#>exception handelling allows the program to handel errors gracefully instead of crashing .

#types:
# zerodivisionError-no. divided by 0
#

#TRY CATCH:
# try:
#     num=int(input("enter a number"))
#     result=100/num
     
# except ValueError:                           #occurs when input of other datatype is entered
#     print("Please enter a valid number")  

# except ZeroDivisionError:                    #occurs when num is 0   
#     print("Number cannot be zero")

# finally:
#     print("Program finished")


# balance=5000
# try:
#     amount=int(input("Enter withdrawal amount"))
#     new_balance=balance-amount
#     print("Remaining Balance:")


student={}
num=int(input("How many students?"))
for i in range(num):
    sub=input("Enter Name of Student:")
    score=list(list(input("Enter the marks:")))
    student[sub]=score
try:
 average=(student.values())/len(student)    
 print(average)
except KeyError:                           #error when we try to acces the value that does not exists
   print("Name of student not found")