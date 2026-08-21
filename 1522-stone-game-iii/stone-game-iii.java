class Solution {
    public String stoneGameIII(int[] stoneValue) {

        int[] dp = new int[stoneValue.length];
        Arrays.fill(dp, -1);

        
        if(solve(stoneValue, 0, dp) > 0){
            return "Alice";
        }else if(solve(stoneValue, 0, dp) < 0){
            return "Bob";
        }else{
            return "Tie";
        }
    }

    private int solve(int[] stoneValue, int i, int[] dp){
        int n = stoneValue.length;
        if(i >= n) return 0;

        if(dp[i] != -1) return dp[i];

        int result = Integer.MIN_VALUE;

        result = Math.max(result, stoneValue[i] - solve(stoneValue, i + 1, dp));

        if(i + 1 < n){
            result = Math.max(result, stoneValue[i] + stoneValue[i + 1] - solve(stoneValue, i + 2, dp));
        }

        if(i + 2 < n){
            result = Math.max(result, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(stoneValue, i + 3, dp));
        }

        return dp[i] = result;
    }
}