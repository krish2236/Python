import random
import string
def generate_username(length=8):
    if length < 4:
        raise ValueError("Username length must be at least 4 characters.")
    letters = string.ascii_lowercase
    digits = string.digits
    all_chars = letters + digits
    username = ''.join(random.choices(all_chars, k=length))
    return username
def main():
    while True:
        try:
            length = int(input("Enter username length: "))
            if length < 4:
                print("Username length must be at least 4 characters.")
                continue
            print("Generated Username:", generate_username(length))
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")
if __name__ == "__main__":
    main()
