# https://afteracademy.com/blog/partition-equal-subset-sum


# O(2^N)
def brute_force(arr):
    if len(arr) == 0:
        return False
    sum = 0
    for elem in arr:
        sum += elem
    if sum % 2 != 0:
        return False
    return is_contain_subset_of_sum(arr, sum / 2)


def is_contain_subset_of_sum(arr, wanted_sum):
    if len(arr) == 1:
        return arr[0] == wanted_sum
    first = arr[0]
    with_first = is_contain_subset_of_sum(arr[1:], wanted_sum - first)
    if with_first:
        return True
    without_first = is_contain_subset_of_sum(arr[1:], wanted_sum)
    if without_first:
        return True
    return False
