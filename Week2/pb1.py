def check_password_strength(password):
    #Python123
    if len(password) < 8:
        return "Weak"
    has_upper = 0
    has_lower = 0
    has_digit = 0
    for letter in password:
        if letter.isupper():
            has_upper = 1

        if letter.islower():
            has_lower = 1

        if letter.isdigit():
            has_digit = 1

    if has_upper == 1 and has_lower == 1 and has_digit == 1:
        return "Strong"
    return "Weak"

print(check_password_strength(input("Enter your password: ")))
