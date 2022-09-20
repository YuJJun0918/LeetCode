###
Given a 1-indexed array of integers numbers that is already 
sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Return their indices if found.
###

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
    start, end = 0, len(numbers) - 1
    
    while True:
      s = numbers[start] + numbers[end]
      
      if s == target:
        return [start + 1, end + 1] #This is because the array is 1-indexed...
      
      if s < target:
        start += 1
      else:
        end -= 1
