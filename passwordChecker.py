password = input("Enter your password: ")

special_chars = "@#$%^&*!"

has_upper = False
has_lower = False
has_digit = False
has_special = False
has_space = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True
    elif ch.isspace():
        has_space = True

if (len(password) >= 8 and has_upper and has_lower
        and has_digit and has_special and not has_space):
    print("Strong Password")
else:
    print("Weak Password")
    