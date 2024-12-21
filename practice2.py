user_val = input("what is the number you would like to check?")
user_val = int(user_val)
if user_val%2 == 0:
    print("Your value is even!\n")
    if user_val%4 == 0:
        print("your value is also divisible by 4!")
else:
    print('Your value is odd!\n')
    if user_val%3 == 0:
        print("your value is also divisible by three!")