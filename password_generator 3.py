import random
import string

def generate_password(length):
    """Generate a random strong password of given length."""
    
    if length < 4:
        return "Password length should be at least 4."

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choice(characters) for _ in range(length))
    
    return password


def main():
    print("===== PASSWORD GENERATOR =====")
    
    try:
        user_length = int(input("Enter desired password length: "))
        result = generate_password(user_length)
        print("Generated Password:", result)
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()