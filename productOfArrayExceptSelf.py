class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    
    l = [1] * len(nums)
    
    pre = 1
    post = 1
    
    for i in range(len(nums)):
      l[i] *= pre
      l[-1-i] *= post
      pre *= nums[i]
      post *= nums[-1-i]
     
    return l
