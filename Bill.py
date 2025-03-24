def calculate_tip():
    try:
        bill = float(input("Enter the total bill amount: "))
        tip_percent = float(input("Enter the tip percentage: "))

        if bill < 0 or tip_percent < 0:
            print("Bill amount and tip percentage must be positive values.")
        else:
            tip = (tip_percent / 100) * bill
            total_bill = bill + tip
            print(f"\nTip amount: ${tip:.2f}")
            print(f"Final bill amount: ${total_bill:.2f}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
calculate_tip()
