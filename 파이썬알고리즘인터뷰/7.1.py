#p7 : find pair of index that get the result by summation

# brute-force solution

def twoSum(nums: list[int], target:int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            