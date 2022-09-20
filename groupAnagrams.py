###
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
###

class Solution(object):
  def groupAnagrams(self, strs):
    
    d = {}
    
    for word in strs:
      key = "".join(sorted(word))
      
      if key in d:
        d[key].append(word)
      else:
        d[key] = [word]
     
    return d.values()
