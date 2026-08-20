class Solution {
    List<String> result = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        StringBuilder curr = new StringBuilder();
        int open = 0;
        int close = 0;
        solve(curr, n, open, close);
        return result;
    }

    private void solve(StringBuilder curr, int n, int open, int close){
        if(curr.length() == 2*n){
            result.add(curr.toString());
            return;
        }

        if(open < n){
        curr.append('(');
        solve(curr, n, open + 1, close);
        curr.deleteCharAt(curr.length() - 1);
        }

        if(close < open){
        curr.append(')');
        solve(curr, n, open, close + 1);
        curr.deleteCharAt(curr.length() - 1);
        }
    }

    // private boolean isValid(StringBuilder str){
    //     int count = 0;
    //     for(char ch : str.toString().toCharArray()){
    //         if(ch == '(') count++;
    //         else count--;
    //         if(count < 0) return false; 
    //     }

    //     return count == 0;
    // }
}