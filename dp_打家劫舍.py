#动态规划，打家劫舍
"""
题目描述：
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
#解题思路：
"""这道题和爬楼梯有点像。MaxObtain[i]表示打劫到第i户时获得的最大金额，可能上一次打劫行动是i-1,i-2,i-3户，但不可能是i-4户，
因为i-4户的情况和i-1，i-2户的情况重复了。相应的分别可以计算打劫到第i户的金额为MaxObtain[i-1],MaxObtain[i-2]+values[i],
和MaxObtain[i-2]+values[i]，取三者最大值。
"""

def rob(values):

n = len(values)
        if n == 0:
            return 0
        elif n == 1:
            return values[0]
        elif n == 2:
            return max(values[0],values[1])
        elif n == 3:
            return max(values[0],values[1],values[2],values[0]+values[2])
        elif n > 3:
            MaxObtain = list(range(n))
            MaxObtain[0] = values[0]
            MaxObtain[1] = values[1]
            MaxObtain[2] = max(values[0],values[1],values[2],values[0]+values[2])
            for i in range(3,n):
                MaxObtain[i] = max(MaxObtain[i-1],MaxObtain[i-2] + values[i],MaxObtain[i-3] + values[i])
            return MaxObtain[-1]

if __name__ == "__main__":
	values1 = input().split(",")#输入格式为2，7,9,3,1
	values = []
	for each in values1:
		values.append(int(each))
	print(rob(values))


