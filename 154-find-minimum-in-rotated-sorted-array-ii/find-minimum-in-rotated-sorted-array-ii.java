class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int low = 0;
        int high = nums.length - 1;
        // int res = Integer.MAX_VALUE;
        while (low <= high){
            int guess = low + (high - low)/2;
            if(nums[guess] > nums[high]){
                low =guess + 1;
            }
            else if(nums[guess] < nums[high]){
                high = guess;
            }
            else{
                high--;
            }
        }
        return nums[low];
    }
}