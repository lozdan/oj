# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > LonelyNumber
# problem url: https://codefights.com/challenge/f4YSm86GMW37drvk6

def LonelyNumber(nums):
    nums = sorted(nums)
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]