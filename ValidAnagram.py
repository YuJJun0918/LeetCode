###
Given a two strings s and t, return True if s is an anagram to t.
###

import collections

class Solution(object):
  def isAnagram(self, s, t):
    
    return Counter(s) == Counter(t)
