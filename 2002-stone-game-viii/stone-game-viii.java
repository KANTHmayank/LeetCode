class Solution {
    int n;
    public int stoneGameVIII(int[] stones) {
        n = stones.length;
        int[] prefixSum = new int[n];
        Arrays.fill(prefixSum, 0);

        prefixSum[0] = stones[0];

        for(int i = 1; i < n; i++){
            prefixSum[i] = prefixSum[i - 1] + stones[i];
        }

        int[] dp = new int[n + 1];
        Arrays.fill(dp, 0);
        // return solve(1, dp, prefixSum);

        dp[n - 1] = prefixSum[n - 1];
        for(int i = n - 2; i >= 1; i--){
            int take = prefixSum[i] - dp[i + 1];
            int skip = dp[i + 1];

            dp[i] = Math.max(take, skip);
        }

        return dp[1];
    }

    // private int solve(int i, int[] dp, int[] prefixSum){
    //     if(i == n-1) return dp[i] = prefixSum[n - 1];

    //     if(dp[i] != Integer.MIN_VALUE) return dp[i];

    //     int take = prefixSum[i] - solve(i + 1, dp, prefixSum);
    //     int skip = solve(i + 1, dp, prefixSum);

    //     return dp[i] = Math.max(take, skip);
    // }
}