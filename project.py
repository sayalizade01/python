#Q.make a project traffic signal using python
# red----> stop
# yellow--->ready
# green----->Go
#anyother colour, please enter valid traffic signal colour

s=input("Enter a colour:").lower()
if s=="Red":
    print("Stop!")
elif s=="Yellow":
    print("Ready!")
elif s=="Green":
    print("Go!")
else: 
     print("Enter valid traffic colour!!!!")