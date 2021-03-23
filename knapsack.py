# given a list of items items (<Weight,Value> pairs) and a weight limit,
# find the best possible value under the weight limit constraint


# O(N*M) where N is the size of the items list and M is the limit
def find(items: list[tuple[int, int]], limit: int):
    n = len(items)
    m = limit + 1
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        item_weight = items[i][0]
        item_value = items[i][1]
        for j in range(m):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                if item_weight <= j:
                    dp[i][j] = item_value
            else:
                best_value_without_current_item = dp[i - 1][j]
                if item_weight <= j:
                    best_value_with_current_item = dp[i - 1][
                        j - item_weight] + item_value
                else:
                    best_value_with_current_item = best_value_without_current_item
                dp[i][j] = max(best_value_with_current_item,
                               best_value_without_current_item)

    print(dp)
    return dp[n - 1][m - 1]
