class Solution {
    
    public int stoneGameII(int[] piles) {
        int[][][] dp = new int[2][101][101];
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 101; j++){
                for(int k = 0; k < 101; k++){
                    dp[i][j][k] = -1;
                }
            }
        }

        return solveForAlice(piles, 1, 0, 1, dp);
    }

    private int solveForAlice(int[] piles, int person, int i, int M, int[][][] dp){
        int n = piles.length;
        if(i >= n) return 0;

        if(dp[person][i][M] != -1){
            return dp[person][i][M];
        }

        int stones = 0;
        int result = (person == 1) ? -1 : Integer.MAX_VALUE;

        for(int x = 1; x <= Math.min(2*M, n - i); x++){
            stones += piles[i + x - 1];

            if(person == 1){
                result = Math.max(result, stones + solveForAlice(piles, 0, i + x, Math.max(M, x), dp));
            }
            else{
                result = Math.min(result, solveForAlice(piles, 1, i + x, Math.max(M, x), dp));
            }
        }
        return dp[person][i][M] = result;
    }
}