def is_palindrome(s):
    return s == s[::-1]

# example
print(is_palindrome("abcdcba")) 
print(is_palindrome("abcde")) 