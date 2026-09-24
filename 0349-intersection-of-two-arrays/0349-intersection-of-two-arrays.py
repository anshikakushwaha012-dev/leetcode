class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1=set(nums1)
        s2=set(nums2)
        ans=[]
        for i in s2:
            if i in s1:
                ans.append(i)
        return ans