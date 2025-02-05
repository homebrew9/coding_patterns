def is_palindrome_valid(s: str) -> bool:    
    # Write your code here
    t = ''.join([ch for ch in s if ch.isalnum()])
    return t == t[::-1]


