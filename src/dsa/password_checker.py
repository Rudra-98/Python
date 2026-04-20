def password_checker(password):
    if len(password) < 8:
        return 0
    elif not any(c.isupper() for c in password):
        return 0
    elif not any(p.islower() for p in password):
        return 0
    elif not any(q.isdigit() for q in password):
        return 0
    elif not any(c in "!@$%^*" for c in password):
        return 0
    return 1


print(password_checker("Hello@123"))
print(password_checker("hello123"))
print(password_checker("HEL@1"))
print(password_checker("Hello@World"))

