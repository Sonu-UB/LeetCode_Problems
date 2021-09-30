def isPalindrome(x):
    if x<0 or (x>0 and x%10==0):
        return False
    s=str(x)
    return s==s[::-1]

x=-121
print(isPalindrome(x))