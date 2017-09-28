

class Solution():
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])


    #Implement an algorithm to determine if a string has all unique characters.
    #What if you can not use additional data structures?
    def uniqueChar(self, s):
        d = dict()
        for each in s:
            d[each] = 0
        for each in s:
            if each in d:
                print("yes")
