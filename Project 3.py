password="Any"
user=str(input("Enter your password: "))
while user != password:
    user=input("Please enter the password correctly: ")
if user == password:
    print("Access granted")
