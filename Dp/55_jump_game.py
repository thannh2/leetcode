class Solution:
	def canJump(self, nums: list[int]) -> bool:
		max_i = -1
		for i in range(len(nums)):
			if i > max_i:
				return False
	
			max_i = max(max_i, i + nums[i])

		return max_i >= len(nums) - 1

if __name__ == "__main__":
	sol = Solution()
	test_case = [3,2,1,0,4]
	print(sol.canJump(test_case))