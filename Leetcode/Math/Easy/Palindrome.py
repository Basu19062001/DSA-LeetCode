"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it 
"""
def is_palindrome(x:int)->bool:
  if x < 0:
    return False
  temp = x
  rev = 0
  while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10
  return temp == rev

def isPalindrome(x:int) -> bool:
  if x < 0:
    return False
  return str(x) == str(x)[::-1]

print(isPalindrome(121))
print(is_palindrome(10))