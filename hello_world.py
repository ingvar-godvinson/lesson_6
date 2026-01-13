password = input('Enter password: ')


def is_long(password):
	is_long = len(password)
	return is_long > 12


def has_digit(password):
	return any(letter.isdigit() for letter in password)


def has_letter(password):
	return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
	return any(letter.isupper() for letter in password)


def has_lower_letters(password):
	return any(letter.islower() for letter in password)


def has_symbols(password):
	return any(not letter.isalnum() for letter in password)


def rate_password(password):
    password_checks = [
        is_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password),
    ]
    password_score = 0
    for password_check in password_checks:
        if password_check:
            password_score += 2
    return password_score

result = rate_password(password)
print('Рейтинг пароля:', result)