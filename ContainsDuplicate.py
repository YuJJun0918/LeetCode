###
Find out if a given list contains any duplicates.
###

class Solution(object):
  def containsDuplicate(self, nums):
    
    if len(set(nums)) != len(nums):
      return True
     else:
      return False
