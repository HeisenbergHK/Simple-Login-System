import sys
from pathlib import Path
import json
from user import User


def test():
    fuck = [{'name': 'Ali', 'id': 2},
            {'name': 'Jafar', 'id': 10}]

    path = Path('test.json')
    content = json.dumps(fuck)
    path.write_text(content)


def load_user_data():
    """This function loads the user data from the json file"""

    path = Path('../user_data.json')

    try:
        content = path.read_text()
    except FileNotFoundError:
        print('Error: There was no file to load!')
        print('The system will automatically make a data file for future usage.')
        empty_user = User('empty', 'empty', -1, 'empty_user', 'empty_password')
        empty_user = empty_user.to_dictionary()
        path.write_text(json.dumps([empty_user]))
        return None
    else:
        user_data = json.loads(content)
        return user_data


def is_user(username):
    """This function checks if the user is in the registered users"""
    for user in data:
        try:
            if user['username'] == username.lower():
                return user
        except TypeError:
            raise TypeError
        except KeyError:
            raise KeyError

    return None


def is_pass(user, password):
    """This function checks is the password correct or not"""

    if user['password'] == password:
        return True
    else:
        return False


def login():
    """This function lets the user log in"""

    print('--Login--')
    print()
    username = input('username: ')

    try:
        user = is_user(username)
    except Exception:
        print('Error: data file is corrupted!')
        print('You may want to check the data file or simply delete it!')
        terminate()

    if not user:
        print('username not found!')
        return None

    attempts = 3
    while True:
        attempts -= 1
        password = input('password: ')

        if is_pass(user, password):
            break

        if attempts <= 0:
            return None

        print(f'You have left {attempts} more attempts.')

    print('You are Now in the System!')


def sign_in():
    """This function takes the user information and stores it in the data file"""

    print('__sign_in__')
    print()

    while True:
        first_name = input('first_name: ')
        if not first_name:
            print('Enter your first name!')
        elif first_name == 'q':
            terminate()
        else:
            break

    while True:
        last_name = input('last_name: ')
        if not last_name:
            print('Enter your last name!')
        if last_name == 'q':
            terminate()
        else:
            break

    while True:
        age = int(input('age: '))

        if not last_name:
            print('Enter your age!')
        elif age <= 0:
            print('Are you kidding me!?')
        elif first_name == 'q':
            terminate()
        else:
            break

    while True:
        username = input('username: ')
        if not is_user(username):
            break
        elif first_name == 'q':
            terminate()
        else:
            print('This username is already taken!')

    while True:
        password = input('password: ')
        if len(password) < 10:
            print('password length must be greater than 9!')
        elif first_name == 'q':
            terminate()
        else:
            break

    print()
    print('Congratulations!')
    print('')

    user = User(first_name.strip(), last_name.strip(), age, username.strip().lower(), password.strip())
    data.append(user.to_dictionary())
    store()


def store():
    """This function updates the data in the file"""

    path = Path('../user_data.json')
    json_formatted = json.dumps(data)
    path.write_text(json_formatted)


def home_page():
    """This function prompts the user with greeting and simple choices"""

    while True:
        print('-----------------------------')
        print('1) login')
        print('2) sign-up')
        print()
        user_input = input('--> ')
        print()

        if user_input == '1':
            login()
        elif user_input == '2':
            sign_in()
        elif user_input == 'q':
            terminate()
        else:
            pass


def terminate():
    """This function terminates the running program"""

    print('-----------------------------')
    print('Good Bye!')
    sys.exit()


print('Welcome to Heisenberg simple login system.')
print('(Enter \'q\' to exit)')

data = load_user_data()

if not data:
    terminate()

home_page()
