class Solution {
    List<String> result = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        StringBuilder curr = new StringBuilder();

        solve(curr, n);
        return result;
    }

    private void solve(StringBuilder curr, int n){
        if(curr.length() == 2*n){
            if(isValid(curr)){
                result.add(curr.toString());

            }
            return;
        }

        curr.append('(');
        solve(curr, n);
        curr.deleteCharAt(curr.length() - 1);

        curr.append(')');
        solve(curr, n);
        curr.deleteCharAt(curr.length() - 1);
    }

    private boolean isValid(StringBuilder str){
        int count = 0;
        for(char ch : str.toString().toCharArray()){
            if(ch == '(') count++;
            else count--;
            if(count < 0) return false; 
        }

        return count == 0;
    }
}