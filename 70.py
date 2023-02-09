class Solution {
    public int climbStairs(int n) {
        
        int[] stairs = new int[46];

        stairs[0] = 0;
        stairs[1] = 1;
        stairs[2] = 2;
        // stairs[3] = 3

        int i = 3;
        while (i<=n){
            stairs[i] = stairs[i-1] + stairs[i-2];
            i++;
        }

        return stairs[n];
        
    }
}