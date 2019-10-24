

is_hot = False
is_cold = False

if is_hot:
    print("it's a hot day")
    print('Drink plenty water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')

else:
    print("It's a lovely day")
print('Enjoy your day')

name_sys = 'Hello world'
print(name_sys.capitalize())
print(name_sys.upper())


name = "reehscueiudcvdgjanxkjlxuhdrehdbscnkwjduwechdsnxkjjchcfdbsjxcnaskcjsdfbhcnasmkdjfh"

if len(name) < 3:
    print('Name must be atleast 3 characters')
elif len(name) > 50:
    print('Name must be a maximum of 50 characters')
else:
    print('Name looks good!')

guess_lim = 1
while guess_lim <= 5:
    print('*' * guess_lim)
    guess_lim = guess_lim + 1
print("Done")


is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
   print("It's a lovely day")
print('Enjoy your day')

has_good_credit = True
has_high_income = True

if has_good_credit and not has_high_income:
    print('Eligible for loan')


temperature = 30

if temperature <= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

secret_number = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Sorry! You failed")












