class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int[] t = new int[n+1];
        // Arrays.fill(t, -1);

        for(int i = n-1; i >= 0; i--){
            
            t[i] = stoneValue[i] - t[i+1];
            

            if(i + 2 <= n){
                t[i] = Math.max(t[i], stoneValue[i] + stoneValue[i+1] - t[i+2]);
            }
            if(i + 3 <= n){
                t[i] = Math.max(t[i], stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - t[i+3]);
            }
        }
        int diff = t[0];
        
        if(diff > 0){
            return "Alice";
        }else if(diff< 0){
            return "Bob";
        }else{
            return "Tie";
        }
    }

    // private int solve(int[] stoneValue, int i, int[] dp){
    //     int n = stoneValue.length;
    //     if(i >= n) return 0;

    //     if(dp[i] != -1) return dp[i];

    //     int result = Integer.MIN_VALUE;

    //     result = Math.max(result, stoneValue[i] - solve(stoneValue, i + 1, dp));

    //     if(i + 1 < n){
    //         result = Math.max(result, stoneValue[i] + stoneValue[i + 1] - solve(stoneValue, i + 2, dp));
    //     }

    //     if(i + 2 < n){
    //         result = Math.max(result, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(stoneValue, i + 3, dp));
    //     }

    //     return dp[i] = result;
    // }
}