def min_cost(costs):
    if not costs or len(costs) == 0:
        return 0
    n = len(costs)
    k = len(costs[0])
    dp = [[0 for _ in range(k)] for _ in range(n)]
    for j in range(k):
        dp[0][j] = costs[0][j]
    for i in range(1, n):
        for j in range(k):
            dp[i][j] = float('inf')
            for l in range(k):
                if j == l:
                    continue
                dp[i][j] = min(dp[i][j], dp[i - 1][l] + costs[i][j])
    result_min_cost = float('inf')
    for j in range(k):
        result_min_cost = min(result_min_cost, dp[n - 1][j])
    return result_min_cost

if __name__ == "__main__":
    costs = [[1, 3, 2], [4, 6, 8], [3, 1, 5]]
    print("Minimum cost:", min_cost(costs))

