from typing import List


# Counting Sort
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:  # O(1)
            return 0

        min_value = min(nums)  # O(n)
        counts = [0 for _ in range(min_value, max(nums) + 1)]  # O(k)

        for v in nums:  # O(n)
            if v != val:
                counts[v - min_value] += 1

        k = 0  # O(1)
        for i in range(len(counts)):  # O(n)
            while counts[i] > 0:
                nums[k] = i + min_value
                counts[i] -= 1
                k += 1

        # O(1) + O(n) + O(k) + O(n) + O(1) + O(n) = O(n)
        return k


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:  # O(n)
            nums.remove(val)  # O(n)
        # O(n^2)
        return len(nums)  # O(1)


def sort(): ...


# [4, 2, 1, 3] -> [1, 2, 3, 4]
#
# [4, 3, 2, 1] -> [1, 2, 3, 4]
# [1, 2, 3, 4] -> [1, 2, 3, 4]


# 1. O(2n^2 + 2n + 1000) = O(n^2)
# 2. O(3n) = O(n)
# 3. O(1000) = O(1)
def msqr(l: list[int]):
    N = len(l)  # 1 * c1 - O(1)
    for i in range(N):  # N * c2 - O(n)
        # l[i] = l[i] * l[i]
        l[i] *= l[i]  # N * c3 - O(n)

    # 0. a = c2 + c3
    # 1. T(N) = 1 * c1 + N * c2 + N * c3 = c1 + N * (c2 + c3) = c1 + a * N
    # 2. T(n) <= C1 * g(n), for all n > n0 then T(n) = O(g(n))
    # 3. c1 + a * N <= C1 * g(n)
    # 4. g(n) = n
    # 5. c1 + a * N <= C1 * n, for all n > n0
    # 6. C1 = a + 1
    # 7. T(n) = O(g(n)) = O(n)


if __name__ == "__main__":
    nums = [0, 0, 0, 0, 0]
    print(nums[3])  # O(1)

    # i * size + base_ptr

    # Now nums has 1,000,000
    print(nums[300_000])  # O(1)
    val = 43
    # print(Solution().removeElement(nums, val))
    # print(nums)
    l = [2, 2, 3]
    nums.insert(2, 10)  # O(n)
    msqr(l)
