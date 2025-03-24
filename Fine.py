due_days = int(input("Enter number of days late: "))

if due_days < 0:
    print("Days late cannot be negative!")
    fine = 0  # Assign fine to avoid errors
else:
    if due_days <= 5:
        fine = due_days * 2
    elif due_days <= 10:
        fine = due_days * 5
    else:
        fine = due_days * 10

    print("Total fine is:", fine)
