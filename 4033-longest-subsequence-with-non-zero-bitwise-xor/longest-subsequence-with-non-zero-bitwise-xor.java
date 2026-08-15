class Solution {
    public int longestSubsequence(int[] nums) {
        int n = nums.length;

        int totalXor = 0;
        boolean allZero = true;

        for(int i : nums){
            totalXor ^= i;

            if(i != 0) {
                allZero = false;
            }
        }
        if(allZero) return 0;

        return (totalXor == 0) ? n-1 : n;
    }
}