age = int(input("Enter your age: ")) 

if age < 0: 
    print("Age cannot be negative!")  
elif age < 5: 
    price = 0 
elif age < 18: 
    price = 10 
elif age < 60: 
    price = 15 
else: 
    price = 12 

print("Your ticket price is $", price)
