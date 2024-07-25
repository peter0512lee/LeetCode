class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = inf

        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue

            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue

            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:
                    if target - s < min_diff:
                        min_diff = target - s
                        ans = s 
                    j += 1
        return ans