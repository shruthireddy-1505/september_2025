class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] >= target:
                h = mid - 1
            else:
                l = mid + 1
        if l < len(nums) and nums[l] == target:
            ans[0] = l

        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        if h >= 0 and nums[h] == target:
            ans[1] = h
        return ans