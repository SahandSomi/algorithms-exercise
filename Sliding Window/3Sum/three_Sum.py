import pytest

class Solution(object):

    def Sum3_SS(self, numbers):

        numbers.sort()
        result = []
        
        for i in range(len(numbers)-2):

            if i>0 and numbers[i] == numbers[i-1]:
                continue

            left, right = i , len(numbers)-1

            while left < right:
                total = numbers[left] + numbers[right] + numbers[i]

                if total < 0:
                    left += 1

                elif total>0:
                    right -= 1

                else:
                    result.append([numbers[i],numbers[left], numbers[right]])

                    while left<right and numbers[left] == numbers[left+1]:
                        left+=1
                    while left< right and numbers[right] == numbers[right-1]:
                        right -=1
                    
                    left += 1
                    right -= 1

        return result
    
    def Sum3_neat(self, nums):
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
            
# Guide for solution:
# Brute Force: all combiunations 3 loops o(n3)
# Sort array nad check for two sum o(nlogn) + O(n2) = O(n2)  space O(1) or O(n) depend on implementation of sorting
### Golden rule: break problem to familiar problem here two sum