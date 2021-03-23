# Given a non-empty array of positive integers arr[]. Write a program to find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1

# Input: arr[] = [1, 6, 11, 6]
# Output: true
# Explanation: The array can be partitioned as [6, 6] and [1, 11].
# Example 2

# Input: arr[] = [2, 6, 7]
# Output: false
# Explanation: The array cannot be partitioned into equal sum sets


def check(arr):
    if len(arr) == 0:
        return False
    sum = 0
    for elem in arr:
        sum += elem
    if sum % 2 != 0:
        return False
    return is_contain_subset_of_sum_dynamic_programming(arr, sum // 2)


# using dynamic programming O(N*M)
# when N is the size of the number list and M is sum of the elements
def is_contain_subset_of_sum_dynamic_programming(arr, wanted_sum):
    n = len(arr)
    m = wanted_sum + 1
    dp = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        num = arr[i]
        for j in range(m):
            if i == 0:
                if arr[i] == j:
                    dp[i][j] = True
            else:
                exist_subset_with_num = dp[i - 1][j - num]
                exist_subset_without_num = dp[i - 1][j]
                if exist_subset_with_num or exist_subset_without_num:
                    dp[i][j] = True
    return dp[n - 1][m - 1]


# Using brute force approach O(2^N)
def is_contain_subset_of_sum_brute_force(arr, wanted_sum):
    if len(arr) == 1:
        return arr[0] == wanted_sum
    first = arr[0]
    with_first = is_contain_subset_of_sum_brute_force(arr[1:],
                                                      wanted_sum - first)
    if with_first:
        return True
    without_first = is_contain_subset_of_sum_brute_force(arr[1:], wanted_sum)
    if without_first:
        return True
    return False
