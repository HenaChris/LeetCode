#动态规划，最大子序和
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

