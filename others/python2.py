class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        z = nums1 + nums2
        l = len(z)
        z.sort()
        if (l%2 == 1) :
            return z[(l/2)]
        else :
            return (z[l//2] + z[l//2 - 1])/2.0
        