import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    # Base character set
    chars = string.ascii_lowercase
    
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    if len(chars) == 0:
        return "No characters selected to generate password."

    # Generate password by random choice
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# User input
if __name__ == "__main__":
    print("🔐 Password Generator")

    length = int(input("Enter password length (e.g., 12): "))
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, digits, special)
    print(f"\nGenerated Password: {password}")
