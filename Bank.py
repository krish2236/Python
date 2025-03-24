balance = 1000  
choice = input("Enter 'D' to deposit, 'W' to withdraw: ").upper()

if choice in ['D', 'W']:
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive!")
        elif choice == 'D':
            balance += amount
            print(f"New balance: ${balance:.2f}")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid amount! Enter a number.")
else:
    print("Invalid transaction! Use 'D' for deposit or 'W' for withdrawal.")
