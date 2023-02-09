class Solution {
    public boolean isPalindrome(int x) {
        // if (x < 0){
        //     return false;
        // }
        char[] y = Integer.toString(x).toCharArray();
        for (int i = 0; i < y.length / 2; i++){
            if (y[i] != y[y.length - 1 - i]){
                return false;
            }
        }
        return true;
    }
}