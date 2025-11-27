def is_palindrome(n):
    if n < 0:
        return False
    return str(n) == str(n)[::-1]

print(is_palindrome("enter integer here"))

