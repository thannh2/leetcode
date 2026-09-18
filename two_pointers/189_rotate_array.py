class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        def reverse(start: int, end: int) -> None:
            while start < end:
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                start += 1
                end -= 1
        k = k%len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) -1)         

if __name__ == "__main__":
    sol = Solution()
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    test_k = 3
    sol.rotate(test_nums, test_k)
    print(f"Ket qua sau khi xoay: {test_nums}")