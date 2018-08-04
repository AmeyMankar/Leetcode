
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def three_sum(self, nums):
        final_ls = []
        temp_ls = []

        for item in nums:
            if item not in temp_ls:
                # print(nums.index(item))
                # temp_ls.append(item)
                temp_ls.append(int(item))
                if sum(temp_ls) == 0:
                    final_ls.append(temp_ls[:])
                if len(temp_ls) == 3:
                    temp_ls.pop(-1)
                    temp_ls.pop(-1)

        print(final_ls)

        return None

nums = input().split()
c = Solution()
c.three_sum(nums)

