import random

def generate_password(num_lower_letters, num_symbols, num_numbers, num_upper_letters):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']

    password_chars = random.sample(symbols, num_symbols) + random.sample(numbers, num_numbers) + random.sample(
        lower_letters, num_lower_letters) + random.sample(upper_letters, num_upper_letters)

    random.shuffle(password_chars)

    password = ''.join(password_chars)
    return password


def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            num_lower_letters = int(input("How many lowercase letters do you want in the password?: "))
            num_symbols = int(input("How many symbols do you want in the password?: "))
            num_numbers = int(input("How many numbers do you want in the password?: "))
            num_upper_letters = int(input("How many uppercase letters do you want in the password?: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        password = generate_password(num_lower_letters, num_symbols, num_numbers, num_upper_letters)

        if password:
            print("Generated Password:", password)
            break


if __name__ == '__main__':
    main()
