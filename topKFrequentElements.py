###
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
###

import collections

class Solution(object):
  def topKFrequent(self, nums, k):
    
    l = list()
    x = Counter(nums).most_common()
    
    for i in x[0:k]:
      l.append(i[0])
      
    return l
