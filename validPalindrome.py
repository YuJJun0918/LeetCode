###
Given a string s, return true if it is a palindrome, or false otherwise.
###

class Solution:
  def isPalindrome(self, s: str) -> bool:
    
    word = ''.join(c for c in s if c.isalnum()).lower()
    
    return word == word[::-1]
