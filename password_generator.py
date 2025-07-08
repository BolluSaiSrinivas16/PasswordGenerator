import random
import string
import re

# 🔐 Password Generator Function
def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        return "No valid character sets selected."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# 🧠 Password Strength Checker
def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    if len(password) >= 16:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 3:
        return "Weak"
    elif score <= 5:
        return "Moderate"
    else:
        return "Strong"

# 🏁 Main Menu
def main():
    print("\n🔐 Password Tool\n")
    print("1. Generate a secure password")
    print("2. Test your own password strength")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        try:
            length = int(input("\nEnter password length (e.g., 12): "))
        except ValueError:
            print("❌ Please enter a valid number.")
            return

        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_special)

        if "No valid character sets" in password:
            print("❌ Cannot generate password: Please select at least one character type.")
        else:
            strength = check_password_strength(password)
            print(f"\n✅ Generated Password: {password}")
            print(f"🔒 Password Strength: {strength}")

    elif choice == '2':
        user_pass = input("\nEnter your password: ").strip()
        strength = check_password_strength(user_pass)
        print(f"🔍 Password Strength: {strength}")

    else:
        print("❌ Invalid option. Please enter 1 or 2.")

# 🧃 Run script
if __name__ == "__main__":
    main()

