import random

def password_generator(uppercase_letter, use_digits, use_special_char, length=8):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#$%^&*|()_+'
    charset = letters
    password = []
    if uppercase_letter:
        charset += letters.upper()
        # this ensures every generated password contains atleast 1 capital letter if chosen
        password.append(random.choice(letters.upper()))
    if use_digits:
        charset += digits
        # this ensures every generated password contains atleast 1 digit if chosen
        password.append(random.choice(digits))
    if use_special_char:
        charset += special_characters
        # this ensures every generated password contains atleast 1 special character
        password.append(random.choice(special_characters))

    remaining_length = length - len(password)
    if remaining_length < 0:
        raise ValueError('Length is too short for selected options')
    password += [random.choice(charset) for _ in range(remaining_length)]

    # ensures that the required characters are not always at the starts
    random.shuffle(password)
    return ''.join(password)

while True:
    print('''-- Password Generator --
          Choose option:
          1. Generate Password
          2. Exit the program''')
    choice = input('Your choice: ')

    if choice == '1':
        try:
            length = int(input('Provide password length: '))
            # converting the user input to boolean
            uppercase_letter = input('Use uppercase letters? (y/n): ').lower() == 'y'
            use_digits = input('Use digits? (y/n): ').lower() == 'y'
            use_special_char = input('Use special characters? (y/n): ').lower() == 'y'

            print(f'Generated password: {password_generator(uppercase_letter, use_digits, use_special_char, length)}')
        except ValueError:
            print('Please enter a valid number!')
    elif choice == '2':
        print('Bye!')
        break
    else:
        print('Please enter a correct value!')


