from password_strength import PasswordPolicy

def check_password_strength(password):
    policy = PasswordPolicy.from_names(
        length=8,
        uppercase=1,
        numbers=1,
        special=1,
    )

    result = policy.test(password)

    if len(result) == 0:
        print(f"The password '{password}' is strong!")
    else:
        print(f"The password '{password}' does not meet the criteria:")
        for crit in result:
            print(crit.get_description())

user_password = input("Enter the password to check its strength: ")
check_password_strength(user_password)
