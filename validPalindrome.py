class Solution:
  def isPalindrome(self, s: str) -> bool:
    
    word = ''.join(c for c in s if c.isalnum()).lower()
    
    return word == word[::-1]
