#动态规划，最大子序和
#题目描述：
"""给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。"""
"""新建一个数组f[n],代表当连续子数组最后一个元素下标为n时，此时子数组的最大和。f[n]=max(f[n-1]+nums[i],nums[i])
"""

def maxSubArray(nums):
    n = len(nums)
    f = list(range(0, n))
    f[0] = nums[0]
    for i in range(1, n):
        f[i] = max(f[i - 1] + nums[i], nums[i])
    return max(f)


if __name__ == "__main__":
    nums1 = input().split(",")
    nums = []
    for each in nums1[1:-2]:
        nums.append(int(each))
    print(maxSubArray(nums))

