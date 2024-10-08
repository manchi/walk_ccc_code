class Solution:
  def mostFrequent(self, nums: list[int], key: int) -> int:
    count = collections.Counter()

    for a, b in zip(nums, nums[1:]):
      if a == key:
        count[b] += 1

    return max(count, key=lambda k: count[k])
