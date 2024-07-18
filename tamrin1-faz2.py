import argparse
import random
import pyautogui
import time

character_alphabet = 'abcdefghijklmnopqrstuvwxyz'
character_number = '0123456789'
character = '0123456789abcdefghijklmnopqrstuvwxyz'
character_list = list(character)
character_number_list = list(character_number)
character_alphabet_list = list(character_alphabet)

def standard_mode():
    password = pyautogui.password('enter your password here')
    n = input('which is search space (alphabet/number/alphanumeric): ')
    number_guess = 0
    guess_password = ''

    start_time = time.time()
    if n.lower() == 'alphabet':
        while (guess_password != password):
            guess_password = random.choices(character_alphabet_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    elif n.lower() == 'number':
        while (guess_password != password):
            guess_password = random.choices(character_number_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    else:
        while (guess_password != password):
            guess_password = random.choices(character_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    exe_time = time.time() - start_time
    print(f'the numbers of guess = {number_guess}')
    print(f'Execution time: {exe_time} sconds')

def firstletter_mode():
    password = pyautogui.password('enter your password here')
    first = input('what is the first letter? ')
    n = input('which is search space (alphabet/number/alphanumeric): ')
    number_guess = 0
    guess_password = first

    start_time = time.time()
    if n.lower() == 'alphabet':
        while (guess_password != password):
            guess_password = random.choices(character_alphabet_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    elif n.lower() == 'number':
        while (guess_password != password):
            guess_password = random.choices(character_number_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    else:
        while (guess_password != password):
            guess_password = random.choices(character_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    exe_time = time.time() - start_time
    print(f'the numbers of guess = {number_guess}')
    print(f'Execution time: {exe_time} sconds')

def kCharacterKnown_mode():
    password = pyautogui.password('enter your password here')
    kCharacter = input('what is k letter? ')
    n = input('which is search space (alphabet/number/alphanumeric):')
    number_guess = 0
    guess_password = kCharacter
    start_time = time.time()
    if n.lower() == 'alphabet':
        while (guess_password != password):
            guess_password = random.choices(character_alphabet_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    elif n.lower() == 'number':
        while (guess_password != password):
            guess_password = random.choices(character_number_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    else:
        while (guess_password != password):
            guess_password = random.choices(character_list, k=len(password))
            number_guess += 1

            if (guess_password == list(password)):
                print('your password is: ' + ''.join(guess_password))
                break
    exe_time = time.time() - start_time
    print(f'the numbers of guess = {number_guess}')
    print(f'Execution time: {exe_time} sconds')


parser = argparse.ArgumentParser(description="Specify mode.")
parser.add_argument("mode", choices=["standard", "firstletter", "kCharacterKnown"], help="Choose a mode: standard, firstletter, or kCharacterKnown.")
parser.add_argument("start", help="Specify 'start' to begin the mode.")

args = parser.parse_args()

if args.mode == 'standard'and args.start == 'mode':
    standard_mode()
elif args.mode == 'firstletter' and args.start == 'mode':
    firstletter_mode()
elif args.mode == 'kCharacterKnown' and args.start == 'mode':
    kCharacterKnown_mode()
