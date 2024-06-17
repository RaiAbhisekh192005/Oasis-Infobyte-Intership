import random
import string

def generate_password(length):
    """Generate a random password of given length."""
    if length < 1:
        raise ValueError("Password length should be at least 1")

    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        
        password = generate_password(length)
        print(f"Generated password: {password}")
        
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
