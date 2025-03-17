def find_largest(num1, num2, num3):
   
    return max(num1, num2, num3)

if __name__ == "__main__":
    
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    number3 = float(input("Enter third number: "))
    print("The largest number is:", find_largest(number1, number2, number3))
