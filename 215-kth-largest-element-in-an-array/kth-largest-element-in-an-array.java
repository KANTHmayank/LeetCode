class Solution {
    public int findKthLargest(int[] nums, int k) {
        
        // int lIndex = 0;
        // while(k > 0){
        //     int largest = nums[lIndex];
        //     int maxIdx = lIndex;
        //     for(int i = lIndex + 1; i < nums.length; i++){
        //         if(nums[i] > largest){
        //             largest = nums[i];
        //             maxIdx = i;
        //             // int lIndex = 0;
                    
                    
        //         }
        //     }
        //     int temp = nums[lIndex];
        //     nums[lIndex] = nums[maxIdx];
        //     nums[maxIdx] = temp;

        //     lIndex++;
        //     k--;
        // }
        // return nums[lIndex - 1];


        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int num : nums){
            if(pq.size() < k) pq.offer(num);
            else if(pq.peek() < num){
                pq.poll();
                pq.offer(num);
            }
        }
        return pq.peek();
    }
}