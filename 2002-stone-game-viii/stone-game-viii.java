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

        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MIN_VALUE);
        return solve(1, dp, prefixSum);
    }

    private int solve(int i, int[] dp, int[] prefixSum){
        if(i == n-1) return dp[i] = prefixSum[n - 1];

        if(dp[i] != Integer.MIN_VALUE) return dp[i];

        int take = prefixSum[i] - solve(i + 1, dp, prefixSum);
        int skip = solve(i + 1, dp, prefixSum);

        return dp[i] = Math.max(take, skip);
    }
}