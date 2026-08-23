class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int leftSum = 0;
        int rightSum = 0;
        int leftQuesCount = 0;
        int rightQuesCount = 0;

        for(int i = 0; i < n; i++){
            if(num.charAt(i) == '?'){
                if(i < n/2){
                    leftQuesCount++;
                }
                else{
                    rightQuesCount++;
                }
            }
            else{
                if(i < n/2){
                    leftSum += num.charAt(i) - '0';
                }
                else{
                    rightSum += num.charAt(i) - '0';
                }
            }
        }

        int totalQuesCount = leftQuesCount + rightQuesCount;

        if(totalQuesCount % 2 == 1) return true;

        int leftTotalSum = 2 * leftSum + 9 * leftQuesCount;
        int rightTotalSum = 2 * rightSum + 9 * rightQuesCount;

        return (leftTotalSum == rightTotalSum) ? false : true;
    }
}