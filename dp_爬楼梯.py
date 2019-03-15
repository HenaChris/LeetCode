#爬楼梯
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
"""
#解析
"""
f[i]为爬到第i阶有多少种方法，它等于f[i-1]+f[i-2]。因为要爬到第i阶，要么从第i-1阶爬到，要么从第i-2阶爬到。
"""
def climbStairs(n):
	if n == 1:
		return 1
	else:
		f = list(range(n))
		f[0] = 1
		f[1] = 2
		for i in range(2,n):
			f[i] = f[i-1] + f[i-2]
		return f[-1]

if __name__ == "__main__":
	n = int(input())
	climbStairs(n)
