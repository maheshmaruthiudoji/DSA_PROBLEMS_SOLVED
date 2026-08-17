"""
1563. Stone Game V
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.
"""
class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        left_pos = [0] * n
        left_best = [0] * n

        right_pos = [None] * n
        right_best = [0] * n

        for l in range(n - 2, -1, -1):
            left_pos[l] = l - 1
            left_best[l] = 0

            for r in range(l + 1, n):
                total = prefix[r + 1] - prefix[l]

                while left_pos[l] + 1 < r:
                    k = left_pos[l] + 1
                    left = prefix[k + 1] - prefix[l]

                    if 2 * left <= total:
                        left_pos[l] = k
                        left_best[l] = max(
                            left_best[l],
                            left + dp[l][k]
                        )
                    else:
                        break

                if right_pos[r] is None:
                    right_pos[r] = r
                    right_best[r] = 0

                while right_pos[r] - 1 >= l:
                    k = right_pos[r] - 1
                    left = prefix[k + 1] - prefix[l]
                    right = total - left

                    if 2 * left >= total:
                        right_pos[r] = k
                        right_best[r] = max(
                            right_best[r],
                            right + dp[k + 1][r]
                        )
                    else:
                        break

                dp[l][r] = max(left_best[l], right_best[r])

        return dp[0][n - 1]